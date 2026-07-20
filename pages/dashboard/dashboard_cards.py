"""
Dashboard Cards
"""

import streamlit as st


class DashboardCards:

    @staticmethod
    def render(stats):

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Questions",
                stats["questions"]
            )

            st.metric(
                "Responses",
                stats["responses"]
            )

        with col2:

            st.metric(
                "Provider",
                stats["provider"]
            )

            st.metric(
                "Model",
                stats["model"]
            )

        with col3:

            st.metric(
                "Temperature",
                stats["temperature"]
            )

            st.metric(
                "Language",
                stats["language"]
            )