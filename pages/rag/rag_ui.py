"""
Enterprise RAG UI
"""

import streamlit as st

from pages.rag.models import (
    SearchType,
    TOP_K_VALUES
)

from pages.rag.rag_service import RAGService
from pages.rag.analytics import RAGAnalytics
from pages.rag.history import RAGHistory
from pages.rag.exporter import RAGExporter
from services.cache_service import CacheService
from services.document_index_service import DocumentIndexService
from services.exception_service import ExceptionService
from services.streaming_service import StreamingService
from services.document_manager_service import DocumentManagerService
from services.analytics_dashboard_service import AnalyticsDashboardService
from services.search_history_service import SearchHistoryService
from services.export_service import ExportService
from services.health_check_service import HealthCheckService
from services.diagnostics_service import DiagnosticsService


class RAGUI:

    @staticmethod
    def render():

        st.title("📚 Enterprise RAG")

        # ==========================================
        # Enterprise RAG UI
        # ==========================================

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
            [
                "🔍 Search",
                "📂 Documents",
                "📊 Dashboard",
                "📈 Analytics",
                "📜 History",
                "📤 Export",
                "⚙️ System"
            ]
        )

        # =====================================================
        # TAB 1
        # =====================================================

        with tab1:

            st.header("🔍 Enterprise Search")

            uploaded_files = st.file_uploader(
                "Upload Documents",
                accept_multiple_files=True
            )

            if uploaded_files:

                if st.button(
                        "Index Documents",
                        key="index_documents"
                ):
                    with st.spinner("Indexing documents..."):
                        stats = DocumentIndexService.index_documents(

                            uploaded_files=uploaded_files,

                            chunk_strategy="Fixed",

                            chunk_size=512,

                            overlap=100

                        )

                    st.success(
                        f"{stats['documents']} document(s) indexed."
                    )

                    st.info(
                        f"Chunks : {stats['chunks']}"
                    )

            st.divider()

            model = st.text_input(
                "Model",
                value="qwen2.5:1.5b"
            )

            search_type = st.selectbox(
                "Search Type",
                [
                    SearchType.SEMANTIC.value,
                    SearchType.KEYWORD.value,
                    SearchType.HYBRID.value,
                    SearchType.REWRITE.value,
                    SearchType.MULTI_QUERY.value,
                    SearchType.HYDE.value,
                    SearchType.PARENT_CHILD.value
                ]
            )

            top_k = st.selectbox(
                "Top K",
                TOP_K_VALUES
            )

            question = st.text_area(
                "Ask a Question"
            )

            if st.button(
                    "Search",
                    key="search_button"
            ):
                with st.spinner("Searching documents..."):

                    if question.strip():

                        try:

                            result = RAGService.ask(

                                question=question,

                                model=model,

                                search_type=search_type,

                                top_k=top_k

                            )

                            RAGHistory.add(

                                question=question,

                                answer=result["answer"],

                                sources=result["sources"]

                            )

                            RAGAnalytics.update(

                                documents=len(result["sources"]),

                                chunks=len(result["citations"]),

                                tokens=result["token_usage"]["tokens"],

                                retrievals=top_k,

                                response_time=result["response_time"],

                                model=model,

                                search_type=search_type

                            )

                            st.session_state["rag_result"] = result

                            st.session_state["rag_result"] = result

                        except Exception as e:

                            error = ExceptionService.handle(e)

                            st.error(error["message"])

            if "rag_result" in st.session_state:

                result = st.session_state["rag_result"]

                st.subheader("💬 AI Answer")

                placeholder = st.empty()

                StreamingService.stream(
                    result["answer"],
                    placeholder
                )

                st.subheader("📂 Parent Documents")

                for parent in result["parents"]:
                    with st.expander(parent["document"]):
                        st.write(parent["text"])

                st.subheader("📚 Sources")

                for source in result["sources"]:
                    with st.expander(source["document"]):
                        st.write(source["text"])

                st.subheader("📖 Citations")

                for citation in result["citations"]:
                    st.write(
                        f"[{citation['id']}] "
                        f"{citation['document']} "
                        f"(Chunk {citation['chunk']})"
                    )

                st.subheader("⚡ Performance")

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Response Time",
                    f"{result['response_time']} ms"
                )

                c2.metric(
                    "Words",
                    result["token_usage"]["words"]
                )

                c3.metric(
                    "Tokens",
                    result["token_usage"]["tokens"]
                )

        # =====================================================
        # TAB 2
        # =====================================================

        with tab2:

            st.header("📂 Document Management")

            documents = DocumentManagerService.get_documents()

            if documents:

                for document in documents:

                    col1, col2, col3 = st.columns([6, 2, 1])

                    col1.write(document["file_name"])

                    col2.write(document["file_type"])

                    if col3.button(
                            "🗑",
                            key=f"delete_{document['id']}"
                    ):
                        DocumentManagerService.delete_document(
                            document["id"]
                        )

                        st.rerun()

            else:

                st.info("No indexed documents.")

            st.divider()

            if st.button(
                    "🔄 Rebuild Index"
            ):
                DocumentManagerService.rebuild_index()

                st.success("Index rebuilt.")

            stats = DocumentManagerService.get_statistics()

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Chunks",
                stats["indexed_chunks"]
            )

            c2.metric(
                "Dimension",
                stats["vector_dimension"]
            )

            c3.metric(
                "Loaded",
                "Yes" if stats["index_loaded"] else "No"
            )

        # =====================================================
        # TAB 3 Dashboard
        # =====================================================

        with tab3:

            st.header("📊 Dashboard")

            stats = AnalyticsDashboardService.statistics()

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Documents",
                stats["documents"]
            )

            c2.metric(
                "Chunks",
                stats["chunks"]
            )

            c3.metric(
                "Searches",
                stats["searches"]
            )

            st.divider()

            index_stats = DocumentManagerService.get_statistics()

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Indexed Chunks",
                index_stats["indexed_chunks"]
            )

            c2.metric(
                "Vector Dimension",
                index_stats["vector_dimension"]
            )

            c3.metric(
                "Index Loaded",
                "Yes" if index_stats["index_loaded"] else "No"
            )

            cache = CacheService.statistics()

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Cache Entries", cache["entries"])

            c2.metric("Hits", cache["hits"])

            c3.metric("Misses", cache["misses"])

            c4.metric("Hit Rate", f"{cache['hit_rate']}%")

        # =====================================================
        # TAB 4 - ANALYTICS
        # =====================================================

        with tab4:

            st.header("📈 Analytics")

            RAGAnalytics.render()

            st.divider()

            st.subheader("Recent Searches")

            history = SearchHistoryService.get_history()

            if history:

                st.dataframe(

                    history,

                    use_container_width=True,

                    hide_index=True

                )

            else:

                st.info("No search history available.")

            st.divider()

            st.subheader("Performance")

            if "rag_result" in st.session_state:

                result = st.session_state["rag_result"]

                c1, c2, c3 = st.columns(3)

                with c1:

                    st.metric(
                        "Response Time",
                        f"{result['response_time']} ms"
                    )

                with c2:

                    st.metric(
                        "Words",
                        result["token_usage"]["words"]
                    )

                with c3:

                    st.metric(
                        "Estimated Tokens",
                        result["token_usage"]["tokens"]
                    )

            else:

                st.info(
                    "Run a search to view performance metrics."
                )

        # =====================================================
        # TAB 5
        # =====================================================

        with tab5:

            st.header("📜 History")

            history = RAGHistory.get()

            for item in reversed(history):
                with st.expander(item["question"]):
                    st.write(item["answer"])

        # =====================================================
        # TAB 6
        # =====================================================

        with tab6:

            st.header("📤 Export")

            if "rag_result" in st.session_state:
                RAGExporter.export_answer(

                    question,

                    st.session_state["rag_result"]["answer"]

                )

            if "chat_history" in st.session_state:
                export = ExportService.export_chat(

                    st.session_state.chat_history

                )

                st.download_button(

                    "Download JSON",

                    export,

                    file_name="chat_history.json",

                    mime="application/json"

                )

        # =====================================================
        # TAB 7
        # =====================================================

        with tab7:

            st.header("⚙️ System")

            health = HealthCheckService.check()

            st.subheader("Health")

            st.write(
                "FAISS Loaded:",
                "✅" if health["faiss_loaded"] else "❌"
            )

            st.write(
                "Dimension:",
                health["dimension"]
            )

            st.divider()

            diagnostics = DiagnosticsService.report()

            st.subheader("Diagnostics")

            st.write(
                "Configuration:",
                "✅ Valid"
                if diagnostics["configuration"]["valid"]
                else "❌ Invalid"
            )

            if diagnostics["configuration"]["errors"]:
                st.error(
                    diagnostics["configuration"]["errors"]
                )

            st.write(
                "Cache Entries:",
                diagnostics["cache_entries"]
            )

            if st.button("🗑 Clear Cache"):
                CacheService.clear()

                st.success("Cache cleared successfully.")

                st.rerun()

            st.write(
                "FAISS Loaded:",
                diagnostics["health"]["faiss_loaded"]
            )
