"""
Enterprise Retrieval Service
"""

from services.embedding_service import EmbeddingService
from services.faiss_service import FAISSService
from services.bm25_service import BM25Service
from services.hybrid_search import HybridSearch
from services.query_rewriter import QueryRewriter
from services.multi_query_service import MultiQueryService
from services.hyde_service import HyDEService
from services.parent_child_retriever import ParentChildRetriever

from services.context_compression import ContextCompression

from services.reranker_service import RerankerService


class RetrievalService:

    def __init__(self):

        self.faiss = FAISSService()

        self.bm25 = BM25Service()

    def build_keyword_index(

        self,

        chunks

    ):

        self.bm25.build(chunks)

    def semantic_search(

        self,

        query,

        top_k=5

    ):

        embedding = EmbeddingService.generate(

            query

        )

        return self.faiss.search(

            embedding,

            top_k

        )

    def keyword_search(

        self,

        query,

        top_k=5

    ):

        return self.bm25.search(

            query,

            top_k

        )

    def hybrid_search(

        self,

        query,

        top_k=5

    ):

        semantic = self.semantic_search(

            query,

            top_k

        )

        keyword = self.keyword_search(

            query,

            top_k

        )

        results = HybridSearch.reciprocal_rank_fusion(

            semantic,

            keyword

        )

        results = RerankerService.rerank(results)

        results = ContextCompression.compress(

            results,

            top_k

        )

        return results

    def parent_child_search(

            self,

            query,

            top_k=5

    ):

        chunks = self.hybrid_search(

            query,

            top_k

        )

        return ParentChildRetriever.retrieve(

            chunks

        )

    def search(

            self,

            query,

            search_type="Hybrid",

            top_k=5

    ):

        if search_type == "Semantic":

            return self.semantic_search(

                query,

                top_k

            )

        elif search_type == "Keyword":

            return self.keyword_search(

                query,

                top_k

            )

        elif search_type == "Hybrid":

            return self.hybrid_search(

                query,

                top_k

            )

        elif search_type == "Rewrite":

            rewritten = self.rewrite_query(query)

            return self.semantic_search(

                rewritten,

                top_k

            )

        elif search_type == "Parent Child":

            return self.parent_child_search(

                query,

                top_k

            )

        elif search_type == "Multi Query":

            return self.multi_query_search(

                query,

                top_k

            )

        elif search_type == "HyDE":

            return self.hyde_search(

                query,

                top_k

            )

        return self.hybrid_search(

            query,

            top_k

        )

    @staticmethod
    def rewrite_query(query):

        return QueryRewriter.rewrite(query)

    def multi_query_search(

            self,

            query,

            top_k=5

    ):

        queries = MultiQueryService.generate(query)

        all_results = []

        for q in queries:
            all_results.extend(

                self.semantic_search(

                    q,

                    top_k

                )

            )

        return all_results

    def hyde_search(

            self,

            query,

            top_k=5

    ):

        hypothetical = HyDEService.generate(query)

        return self.semantic_search(

            hypothetical,

            top_k

        )

