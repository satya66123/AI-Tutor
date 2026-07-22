"""
Coding Tutor Analytics
"""

import streamlit as st


class CodingAnalytics:

    @staticmethod
    def initialize():

        if "coding_requests" not in st.session_state:
            st.session_state.coding_requests = 0

    @staticmethod
    def render(code):

        CodingAnalytics.initialize()

        lines = len(code.splitlines())

        words = len(code.split())

        characters = len(code)

        st.divider()

        st.subheader("📊 Coding Analytics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Lines", lines)

        with col2:
            st.metric("Words", words)

        with col3:
            st.metric("Characters", characters)

        with col4:
            st.metric(
                "Requests",
                st.session_state.coding_requests
            )