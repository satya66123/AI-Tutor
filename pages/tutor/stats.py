"""
Chat Statistics
"""

import streamlit as st


class ChatStats:

    @staticmethod
    def render():

        messages = st.session_state.get(
            "messages",
            []
        )

        users = sum(
            1 for m in messages
            if m["role"] == "user"
        )

        assistants = sum(
            1 for m in messages
            if m["role"] == "assistant"
        )

        st.divider()

        st.subheader("💬 Chat Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Questions", users)

        with col2:
            st.metric("Responses", assistants)