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

        st.sidebar.divider()

        st.sidebar.caption("### Chat Statistics")

        st.sidebar.metric(
            "Questions",
            users
        )

        st.sidebar.metric(
            "Responses",
            assistants
        )