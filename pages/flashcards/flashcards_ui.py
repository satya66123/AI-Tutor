"""
Flashcards UI
"""

import streamlit as st

from pages.flashcards.analytics import FlashcardsAnalytics
from pages.flashcards.exporter import FlashcardsExporter
from pages.flashcards.history import FlashcardsHistory
from pages.flashcards.models import DIFFICULTIES
from pages.flashcards.flashcards_service import FlashcardsService
from pages.flashcards.parser import FlashcardParser

from services.model_service import ModelService

from utils.error_handler import ErrorHandler


class FlashcardsUI:

    @staticmethod
    def initialize():

        if "flashcards" not in st.session_state:
            st.session_state.flashcards = []

        if "current_card" not in st.session_state:
            st.session_state.current_card = 0

        if "show_back" not in st.session_state:
            st.session_state.show_back = False

    @staticmethod
    def render():

        FlashcardsUI.initialize()

        st.title("📚 AI Flashcards")

        st.write(
            "Generate AI-powered flashcards using Ollama, OpenAI, or Anthropic."
        )

        st.divider()

        topic = st.text_input(
            "📖 Topic",
            placeholder="Example: Python, Java, AI"
        )

        difficulty = st.selectbox(
            "Difficulty",
            DIFFICULTIES
        )

        cards = st.slider(
            "Number of Flashcards",
            min_value=5,
            max_value=30,
            value=10
        )

        models = ModelService.get_models()

        default_index = 0

        model = st.selectbox(
            "AI Model",
            models,
            index=default_index
        )

        if st.button(
            "🚀 Generate Flashcards",
            use_container_width=True
        ):

            if topic.strip() == "":

                st.warning("Please enter a topic.")

                return

            try:

                with st.spinner("Generating Flashcards..."):

                    response = FlashcardsService.generate(
                        topic=topic,
                        difficulty=difficulty,
                        cards=cards,
                        model=model
                    )

                flashcards = FlashcardParser.extract(
                    response
                )

                st.session_state.flashcards = flashcards
                st.session_state.current_card = 0
                st.session_state.show_back = False

                st.success("Flashcards Generated Successfully")

                FlashcardsHistory.add(
                    topic,
                    flashcards
                )

            except Exception as e:

                ErrorHandler.handle(e)

        if len(st.session_state.flashcards) > 0:

            st.divider()

            total = len(
                st.session_state.flashcards
            )

            current = st.session_state.current_card

            card = st.session_state.flashcards[current]

            st.subheader(
                f"Card {current + 1} / {total}"
            )

            if st.session_state.show_back:

                st.info(card["back"])

            else:

                st.success(card["front"])

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button("⬅ Previous"):

                    if current > 0:

                        st.session_state.current_card -= 1
                        st.session_state.show_back = False
                        st.rerun()

            with col2:

                if st.button("🔄 Flip"):

                    st.session_state.show_back = \
                        not st.session_state.show_back

                    st.rerun()

            with col3:

                if st.button("Next ➡"):

                    if current < total - 1:

                        st.session_state.current_card += 1
                        st.session_state.show_back = False
                        st.rerun()

            st.divider()

            FlashcardsExporter.download_txt(
                st.session_state.flashcards
            )

            FlashcardsExporter.download_json(
                st.session_state.flashcards
            )

            st.divider()

            FlashcardsAnalytics.render(
                st.session_state.flashcards
            )

            st.divider()

            if st.checkbox("Show Flashcards History"):

                history = FlashcardsHistory.get()

                if not history:

                    st.info("No flashcards generated.")

                else:

                    for item in reversed(history):

                        with st.expander(item["topic"]):

                            for index, card in enumerate(
                                    item["cards"],
                                    start=1
                            ):
                                st.write(f"**Card {index}**")
                                st.write(f"Front: {card['front']}")
                                st.write(f"Back : {card['back']}")
                                st.divider()