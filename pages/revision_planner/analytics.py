"""
Planner Analytics
"""

import streamlit as st


class PlannerAnalytics:

    @staticmethod
    def initialize():

        if "planner_requests" not in st.session_state:

            st.session_state.planner_requests = 0

    @staticmethod
    def render(plan):

        PlannerAnalytics.initialize()

        words = len(plan.split())

        lines = len(plan.splitlines())

        st.divider()

        st.subheader("📊 Planner Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Words",

                words

            )

        with col2:

            st.metric(

                "Lines",

                lines

            )

        with col3:

            st.metric(

                "Plans Generated",

                st.session_state.planner_requests

            )