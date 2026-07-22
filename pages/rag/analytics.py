"""
Enterprise RAG Analytics
"""

import streamlit as st


class RAGAnalytics:

    @staticmethod
    def initialize():

        defaults = {

            "rag_queries": 0,
            "rag_documents": 0,
            "rag_chunks": 0,
            "rag_tokens": 0,
            "rag_retrievals": 0,
            "rag_response_time": 0.0,
            "rag_last_model": "",
            "rag_last_search_type": ""

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    @staticmethod
    def update(

        documents=0,
        chunks=0,
        tokens=0,
        retrievals=0,
        response_time=0,
        model="",
        search_type=""

    ):

        RAGAnalytics.initialize()

        st.session_state.rag_queries += 1
        st.session_state.rag_documents += documents
        st.session_state.rag_chunks += chunks
        st.session_state.rag_tokens += tokens
        st.session_state.rag_retrievals += retrievals
        st.session_state.rag_response_time = response_time
        st.session_state.rag_last_model = model
        st.session_state.rag_last_search_type = search_type

    @staticmethod
    def render():

        RAGAnalytics.initialize()

        st.subheader("📈 RAG Analytics")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Queries",
                st.session_state.rag_queries
            )

        with c2:
            st.metric(
                "Documents",
                st.session_state.rag_documents
            )

        with c3:
            st.metric(
                "Chunks",
                st.session_state.rag_chunks
            )

        c4, c5, c6 = st.columns(3)

        with c4:
            st.metric(
                "Retrievals",
                st.session_state.rag_retrievals
            )

        with c5:
            st.metric(
                "Estimated Tokens",
                st.session_state.rag_tokens
            )

        with c6:
            st.metric(
                "Response Time",
                f"{st.session_state.rag_response_time} ms"
            )

        st.divider()

        st.subheader("Current Session")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                "**Model:**",
                st.session_state.rag_last_model
            )

        with col2:

            st.write(
                "**Search Type:**",
                st.session_state.rag_last_search_type
            )