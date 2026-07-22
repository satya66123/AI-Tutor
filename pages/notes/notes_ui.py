"""
Notes UI
"""

import streamlit as st

from pages.notes.models import (
    NOTE_TYPES,
    DIFFICULTIES
)

from pages.notes.notes_service import NotesService
from pages.notes.exporter import NotesExporter
from pages.notes.history import NotesHistory
from pages.notes.analytics import NotesAnalytics

from services.model_service import ModelService

from utils.error_handler import ErrorHandler


class NotesUI:

    @staticmethod
    def initialize():

        if "notes" not in st.session_state:
            st.session_state.notes = ""

        if "notes_generated" not in st.session_state:
            st.session_state.notes_generated = False

    @staticmethod
    def render():

        NotesUI.initialize()

        st.title("📝 AI Notes Generator")

        st.write(
            "Generate AI-powered study notes using Ollama, OpenAI, or Anthropic."
        )

        st.divider()

        topic = st.text_input(
            "📚 Topic",
            placeholder="Example: Python, Machine Learning"
        )

        col1, col2 = st.columns(2)

        with col1:

            note_type = st.selectbox(
                "Notes Type",
                NOTE_TYPES
            )

        with col2:

            difficulty = st.selectbox(
                "Difficulty",
                DIFFICULTIES
            )

        words = st.slider(
            "Approximate Words",
            min_value=100,
            max_value=2000,
            value=500,
            step=100
        )

        models = ModelService.get_models()

        model = st.selectbox(
            "AI Model",
            models
        )

        generate = st.button(
            "🚀 Generate Notes",
            use_container_width=True
        )

        if generate:

            if topic.strip() == "":

                st.warning("Please enter a topic.")

                return

            try:

                with st.spinner("Generating Notes..."):

                    notes = NotesService.generate(
                        topic=topic,
                        note_type=note_type,
                        difficulty=difficulty,
                        words=words,
                        model=model
                    )

                st.session_state.notes = notes
                st.session_state.notes_generated = True

                NotesHistory.add(notes)

                st.success("Notes Generated Successfully")

            except Exception as e:

                ErrorHandler.handle(e)

                return

        if st.session_state.notes_generated:

            st.divider()

            st.subheader("📄 Generated Notes")

            st.markdown(st.session_state.notes)

            st.divider()

            NotesExporter.download(
                st.session_state.notes
            )

            st.divider()

            NotesAnalytics.render(
                st.session_state.notes
            )

        st.divider()

        if st.checkbox("Show Notes History"):

            history = NotesHistory.get()

            if len(history) == 0:

                st.info("No notes generated yet.")

            else:

                for index, notes in enumerate(
                    reversed(history),
                    start=1
                ):

                    with st.expander(f"Notes {index}"):

                        st.markdown(notes)

        st.divider()

        if st.button(
            "🗑 Clear Notes",
            use_container_width=True
        ):

            st.session_state.notes = ""
            st.session_state.notes_generated = False

            st.rerun()