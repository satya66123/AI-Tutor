"""
Learning Analytics Service
"""

import streamlit as st


class LearningAnalyticsService:

    @staticmethod
    def get_data():

        messages = st.session_state.get(
            "messages",
            []
        )

        questions = sum(
            1
            for m in messages
            if m["role"] == "user"
        )

        responses = sum(
            1
            for m in messages
            if m["role"] == "assistant"
        )

        return {

            "questions": questions,

            "responses": responses,

            "quizzes": st.session_state.get(
                "quiz_attempts",
                0
            ),

            "quiz_score": st.session_state.get(
                "quiz_score",
                0
            ),

            "flashcards": len(

                st.session_state.get(
                    "flashcards_history",
                    []
                )

            ),

            "notes": len(

                st.session_state.get(
                    "notes_history",
                    []
                )

            ),

            "pdfs": len(

                st.session_state.get(
                    "pdf_history",
                    []
                )

            ),

            "pdf_questions": st.session_state.get(
                "pdf_questions",
                0
            ),

            "coding": st.session_state.get(
                "coding_requests",
                0
            ),

            "planner": st.session_state.get(
                "planner_requests",
                0
            )

        }