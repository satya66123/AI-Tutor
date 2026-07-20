"""
Quiz Export
"""

import streamlit as st


class QuizExporter:

        @staticmethod
        def download_quiz(text):
            st.download_button(
                "📥 Download Quiz",
                text,
                "quiz.txt"
            )

        @staticmethod
        def download_result(result):
            st.download_button(

                "📊 Download Result",

                str(result),

                "quiz_result.txt"
            )

