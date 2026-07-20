"""
Quiz Service
"""

import streamlit as st

from services.chat_service import ChatService
from pages.quiz.prompt_builder import QuizPromptBuilder


class QuizService:

    @staticmethod
    def generate(
        topic,
        difficulty,
        quiz_type,
        questions,
        model
    ):

        prompt = QuizPromptBuilder.build(
            topic,
            difficulty,
            quiz_type,
            questions
        )

        # DEBUG
        #st.subheader("Prompt Sent to AI")
        #st.code(prompt)

        response = ChatService.generate_response(
            prompt=prompt,
            model=model
        )

        #st.subheader("Raw AI Response")
        #st.code(response)

        return response