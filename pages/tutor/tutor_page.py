"""
Tutor Page
"""

import streamlit as st

from pages.tutor.chat_ui import ChatUI
from pages.tutor.chat_history import ChatHistory
from pages.tutor.exporter import ChatExporter


class TutorPage:

    @staticmethod
    def render(model):

        ChatHistory.initialize()

        st.subheader("🎓 AI Tutor")

        col1, col2, col3 = st.columns([6, 1, 1])

        with col2:

            if st.button("🗑 Clear"):

                ChatHistory.clear()

                st.rerun()

        with col3:

            ChatExporter.export(
                ChatHistory.get_messages()
            )

        ChatUI.render(model)