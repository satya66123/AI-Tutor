"""
Header Component
"""

import streamlit as st


class Header:

    @staticmethod
    def render():

        st.title("🎓 AI Tutor")

        st.caption(
            "Your Intelligent Learning Assistant"
        )

        st.divider()