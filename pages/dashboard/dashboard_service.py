"""
Dashboard Service
"""

import streamlit as st


class DashboardService:

    @staticmethod
    def get_statistics():

        messages = st.session_state.get("messages", [])

        settings = st.session_state.get("settings", {})

        user_messages = sum(
            1 for m in messages
            if m["role"] == "user"
        )

        assistant_messages = sum(
            1 for m in messages
            if m["role"] == "assistant"
        )

        return {
            "questions": user_messages,
            "responses": assistant_messages,
            "provider": st.session_state.get(
                "provider",
                "ollama"
            ),
            "model": st.session_state.get(
                "model",
                "N/A"
            ),
            "temperature": settings.get(
                "temperature",
                0.7
            ),
            "language": settings.get(
                "language",
                "English"
            )
        }