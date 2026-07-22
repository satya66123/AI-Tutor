import streamlit as st


class PDFHistory:

    @staticmethod
    def initialize():

        if "pdf_history" not in st.session_state:
            st.session_state.pdf_history = []

        if "pdf_questions" not in st.session_state:
            st.session_state.pdf_questions = 0

        if "pdf_answers" not in st.session_state:
            st.session_state.pdf_answers = 0

    @staticmethod
    def add(pdf_name):

        PDFHistory.initialize()

        st.session_state.pdf_history.append(pdf_name)

    @staticmethod
    def add_question():

        PDFHistory.initialize()

        st.session_state.pdf_questions += 1

    @staticmethod
    def add_answer():

        PDFHistory.initialize()

        st.session_state.pdf_answers += 1

    @staticmethod
    def get():

        PDFHistory.initialize()

        return st.session_state.pdf_history