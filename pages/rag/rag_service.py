"""
Enterprise RAG Service
"""

from services.cache_service import CacheService
from services.retreival_service import RetrievalService
from services.chat_service import ChatService
from pages.rag.prompt_builder import RAGPromptBuilder
from pages.rag.models import SearchType
from services.memory_service import MemoryService
from services.citation_service import CitationService
from services.session_service import SessionService
from services.response_time_service import ResponseTimeService
from services.token_usage_service import TokenUsageService
from services.mysql_service import MySQLService


class RAGService:

    @staticmethod
    def ask(
            question,
            model,
            search_type,
            top_k
    ):

        provider = "Ollama"

        # -----------------------------
        # Cache Key
        # -----------------------------
        cache_key = (
            f"{model}:"
            f"{search_type}:"
            f"{top_k}:"
            f"{question.strip().lower()}"
        )

        # -----------------------------
        # Check Cache
        # -----------------------------
        cached = CacheService.get(cache_key)

        if cached:
            return cached

        # -----------------------------
        # Retrieve Documents
        # -----------------------------
        retrieval = RetrievalService()

        retrieved = retrieval.search(
            query=question,
            search_type=search_type,
            top_k=top_k
        )

        parents = []
        sources = []

        if search_type == SearchType.PARENT_CHILD.value:

            parents = retrieved

            context = "\n\n".join(
                parent["text"]
                for parent in parents
            )

            for parent in parents:
                sources.extend(parent["chunks"])

        else:

            sources = retrieved

            context = "\n\n".join(
                chunk["text"]
                for chunk in sources
            )

        # -----------------------------
        # Conversation Memory
        # -----------------------------
        memory = MemoryService.get_context()

        # -----------------------------
        # Build Prompt
        # -----------------------------
        prompt = RAGPromptBuilder.build(
            question,
            context,
            memory
        )

        # -----------------------------
        # Generate Response
        # -----------------------------
        start_time = ResponseTimeService.start()

        answer = ChatService.generate_response(
            prompt=prompt,
            model=model
        )

        response_time = ResponseTimeService.stop(start_time)

        # -----------------------------
        # Save Memory
        # -----------------------------
        MemoryService.add(
            question,
            answer
        )

        # -----------------------------
        # Token Usage
        # -----------------------------
        usage = TokenUsageService.estimate(answer)

        # -----------------------------
        # Citations
        # -----------------------------
        citations = CitationService.build(
            sources
        )

        # -----------------------------
        # Save Retrieval History
        # -----------------------------
        MySQLService.execute(
            """
            INSERT INTO retrieval_history
            (
                query,
                total_results,
                response_time,
                provider,
                model,
                search_type
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                question,
                len(sources),
                response_time,
                provider,
                model,
                search_type
            )
        )

        # -----------------------------
        # Session
        # -----------------------------
        session_id = SessionService.create()

        # -----------------------------
        # Final Result
        # -----------------------------
        result = {

            "session_id": session_id,

            "answer": answer,

            "sources": sources,

            "parents": parents,

            "citations": citations,

            "search_type": search_type,

            "response_time": response_time,

            "token_usage": usage

        }

        # -----------------------------
        # Save Cache (stores JSON)
        # -----------------------------
        CacheService.set(

            cache_key,

            question,

            result,

            provider,

            model

        )

        # -----------------------------
        # Save Search History
        # -----------------------------
        MySQLService.save_search(

            question,

            answer,

            len(sources),

            response_time,

            provider,

            model,

            search_type

        )

        return result