"""
Quiz UI
"""

import streamlit as st

from pages.quiz.models import (
    QUIZ_TYPES,
    DIFFICULTIES
)

from pages.quiz.quiz_service import QuizService
from pages.quiz.history import QuizHistory
from pages.quiz.exporter import QuizExporter
from pages.quiz.parser import QuizParser
from pages.quiz.evaluator import QuizEvaluator
from pages.quiz.analytics import QuizAnalytics

from services.model_service import ModelService

from utils.error_handler import ErrorHandler


class QuizUI:

    @staticmethod
    def initialize():

        if "quiz" not in st.session_state:
            st.session_state.quiz = ""

        if "answer_key" not in st.session_state:
            st.session_state.answer_key = {}

        if "quiz_generated" not in st.session_state:
            st.session_state.quiz_generated = False

    @staticmethod
    def render():

        QuizUI.initialize()

        st.title("📝 AI Quiz Generator")

        st.write(
            "Generate AI-powered quizzes using Ollama, OpenAI, or Anthropic."
        )

        st.divider()

        topic = st.text_input(
            "📚 Topic",
            placeholder="Example: Python, Java, Machine Learning"
        )

        col1, col2 = st.columns(2)

        with col1:

            difficulty = st.selectbox(
                "Difficulty",
                DIFFICULTIES
            )

        with col2:

            quiz_type = st.selectbox(
                "Quiz Type",
                QUIZ_TYPES
            )

        questions = st.slider(
            "Number of Questions",
            min_value=5,
            max_value=30,
            value=10
        )

        models = ModelService.get_models()

        model = st.selectbox(
            "AI Model",
            models
        )

        generate = st.button(
            "🚀 Generate Quiz",
            use_container_width=True
        )

        if generate:

            if topic.strip() == "":

                st.warning("Please enter a topic.")

                return

            try:

                with st.spinner("Generating Quiz..."):

                    quiz = QuizService.generate(
                        topic=topic,
                        difficulty=difficulty,
                        quiz_type=quiz_type,
                        questions=questions,
                        model=model
                    )

                st.session_state.quiz = quiz

                answer_key = QuizParser.extract_answers(
                    quiz
                )

                st.session_state.quiz = quiz

                answer_key = QuizParser.extract_answers(quiz)

                st.session_state.quiz = quiz
                st.session_state.answer_key = answer_key
                st.session_state.quiz_generated = True
                st.session_state.total_questions = questions

                QuizHistory.add(quiz)

                st.success("Quiz Generated Successfully")

            except Exception as e:

                ErrorHandler.handle(e)

                return

        if st.session_state.quiz_generated:

            st.divider()

            st.subheader("📄 Generated Quiz")

            quiz_text = st.session_state.quiz

            if "Answer Key" in quiz_text:

                questions_only = quiz_text.split("Answer Key")[0]

            else:

                questions_only = quiz_text

            st.markdown(questions_only)

            QuizExporter.download_quiz(
                questions_only
            )

            st.divider()

            st.subheader("✍ Submit Your Answers")

            user_answers = {}

            for number in st.session_state.answer_key.keys():

                user_answers[number] = st.text_input(
                    f"Answer {number}"
                )

            if st.button(
                "✅ Evaluate Quiz",
                use_container_width=True
            ):

                result = QuizEvaluator.evaluate(
                    user_answers,
                    st.session_state.answer_key
                )

                QuizAnalytics.render(result)

                QuizExporter.download_result(result)

            st.divider()

            if st.checkbox("Show Answer Key"):

                st.json(
                    st.session_state.answer_key
                )

        st.divider()

        if st.checkbox("Show Quiz History"):

            QuizHistory.initialize()

            if len(st.session_state.quiz_history) == 0:

                st.info("No quizzes generated yet.")

            else:

                for index, quiz in enumerate(
                    reversed(st.session_state.quiz_history),
                    start=1
                ):

                    with st.expander(f"Quiz {index}"):

                        st.markdown(quiz)

        st.divider()

        if st.button(
            "🗑 Clear Quiz",
            use_container_width=True
        ):

            st.session_state.quiz = ""
            st.session_state.answer_key = {}
            st.session_state.quiz_generated = False

            st.rerun()