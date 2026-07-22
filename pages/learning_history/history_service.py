"""
Learning History Service
"""

import streamlit as st


class LearningHistoryService:

    @staticmethod
    def get_all():

        return {

            "Chat":

            st.session_state.get(
                "messages",
                []
            ),

            "Quiz":

            st.session_state.get(
                "quiz_history",
                []
            ),

            "Flashcards":

            st.session_state.get(
                "flashcards_history",
                []
            ),

            "Notes":

            st.session_state.get(
                "notes_history",
                []
            ),

            "PDF":

            st.session_state.get(
                "pdf_history",
                []
            ),

            "Coding":

            st.session_state.get(
                "coding_history",
                []
            ),

            "Planner":

            st.session_state.get(
                "planner_history",
                []
            )

        }