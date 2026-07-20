"""
Planner UI
"""

import streamlit as st

from pages.planner.planner_service import PlannerService
from pages.planner.exporter import PlannerExporter


class PlannerUI:

    @staticmethod
    def render(model):

        st.subheader("📚 Study Planner")

        subject = st.text_input(
            "Subject"
        )

        level = st.selectbox(
            "Current Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        goal = st.text_area(
            "Learning Goal"
        )

        hours = st.number_input(
            "Hours Per Day",
            1,
            12,
            2
        )

        duration = st.selectbox(
            "Duration",
            [
                "1 Week",
                "2 Weeks",
                "1 Month",
                "2 Months",
                "3 Months",
                "6 Months"
            ]
        )

        if st.button("Generate Study Plan"):

            if not subject:

                st.warning(
                    "Please enter a subject."
                )

                return

            with st.spinner(
                "Generating Study Plan..."
            ):

                plan = PlannerService.generate(
                    subject,
                    level,
                    goal,
                    hours,
                    duration,
                    model
                )

            st.markdown(plan)

            PlannerExporter.export(plan)