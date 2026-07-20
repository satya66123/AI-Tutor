"""
Quiz History
"""

import streamlit as st


class QuizHistory:

    @staticmethod
    def initialize():

        if "quiz_history" not in st.session_state:
            st.session_state.quiz_history = []

    @staticmethod
    def add(quiz):

        QuizHistory.initialize()

        st.session_state.quiz_history.append(quiz)