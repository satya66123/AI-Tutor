"""
PDF Analytics
"""

import streamlit as st


class PDFAnalytics:

    @staticmethod
    def initialize():

        if "pdf_questions" not in st.session_state:
            st.session_state.pdf_questions = 0

        if "pdf_answers" not in st.session_state:
            st.session_state.pdf_answers = 0

    @staticmethod
    def render(text, chunks):

        PDFAnalytics.initialize()

        st.divider()

        st.subheader("📊 PDF Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Words",
                len(text.split())
            )

        with col2:
            st.metric(
                "Characters",
                len(text)
            )

        with col3:
            st.metric(
                "Chunks",
                len(chunks)
            )

        st.divider()

        st.subheader("📈 Usage Analytics")

        col4, col5 = st.columns(2)

        with col4:
            st.metric(
                "Questions Asked",
                st.session_state.pdf_questions
            )

        with col5:
            st.metric(
                "Answers Generated",
                st.session_state.pdf_answers
            )