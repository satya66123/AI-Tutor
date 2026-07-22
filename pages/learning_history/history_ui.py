"""
Learning History UI
"""

import streamlit as st

from pages.learning_history.history_service import (
    LearningHistoryService
)

from pages.learning_history.exporter import (
    HistoryExporter
)


class LearningHistoryUI:

    @staticmethod
    def render():

        st.title("📚 Learning History")

        st.write(
            "View all AI Tutor activity."
        )

        history = LearningHistoryService.get_all()

        search = st.text_input(
            "🔍 Search History"
        )

        st.divider()

        for section, items in history.items():

            st.subheader(section)

            if not items:

                st.info("No history found.")

                continue

            for item in items:

                text = str(item)

                if search:

                    if search.lower() not in text.lower():

                        continue

                st.write(text)

            st.divider()

        HistoryExporter.download(history)