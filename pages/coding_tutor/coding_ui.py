"""
Coding Tutor UI
"""

import streamlit as st

from pages.coding_tutor.models import (
    LANGUAGES,
    TASKS
)

from pages.coding_tutor.coding_service import CodingTutorService
from pages.coding_tutor.exporter import CodingExporter
from pages.coding_tutor.analytics import CodingAnalytics
from pages.coding_tutor.history import CodingHistory

from services.model_service import ModelService
from utils.error_handler import ErrorHandler


class CodingTutorUI:

    @staticmethod
    def initialize():

        defaults = {

            "coding_result": "",

            "coding_requests": 0

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    @staticmethod
    def render():

        CodingTutorUI.initialize()

        st.title("💻 AI Coding Tutor")

        st.write(
            "Explain, debug, optimize and generate code using AI."
        )

        st.divider()

        language = st.selectbox(

            "Programming Language",

            LANGUAGES

        )

        task = st.selectbox(

            "Task",

            TASKS

        )

        models = ModelService.get_models()

        model = st.selectbox(

            "AI Model",

            models

        )

        code = st.text_area(

            "Enter Code",

            height=350,

            placeholder="Paste or type your code here..."

        )

        if st.button(

            "🚀 Process",

            use_container_width=True

        ):

            if not code.strip():

                st.warning("Please enter some code.")

                st.stop()

            try:

                with st.spinner("AI is processing your code..."):

                    result = CodingTutorService.process(

                        task=task,

                        language=language,

                        code=code,

                        model=model

                    )

                st.session_state.coding_result = result

                st.session_state.coding_requests += 1

                CodingHistory.add(

                    task,

                    language

                )

            except Exception as e:

                ErrorHandler.handle(e)

                return

        if st.session_state.coding_result:

            st.divider()

            st.subheader("🤖 AI Result")

            st.markdown(

                st.session_state.coding_result

            )

            CodingExporter.download(

                st.session_state.coding_result

            )

            CodingAnalytics.render(

                code

            )

        st.divider()

        if st.checkbox(

            "Show History"

        ):

            history = CodingHistory.get()

            if history:

                for item in reversed(history):

                    st.write(

                        f"• {item['task']} ({item['language']})"

                    )

            else:

                st.info(

                    "No history available."

                )

        st.divider()

        if st.button(

            "🗑 Clear",

            use_container_width=True

        ):

            st.session_state.coding_result = ""

            st.session_state.coding_requests = 0

            st.rerun()