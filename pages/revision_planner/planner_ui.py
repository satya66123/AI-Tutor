"""
Revision Planner UI
"""

import streamlit as st

from pages.revision_planner.models import (
    DIFFICULTIES,
    GOALS,
    PLAN_TYPES
)

from pages.revision_planner.planner_service import RevisionPlannerService
from pages.revision_planner.exporter import PlannerExporter
from pages.revision_planner.analytics import PlannerAnalytics
from pages.revision_planner.history import PlannerHistory

from services.model_service import ModelService
from utils.error_handler import ErrorHandler


class PlannerUI:

    @staticmethod
    def initialize():

        defaults = {

            "revision_plan": "",

            "planner_requests": 0

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    @staticmethod
    def render():

        PlannerUI.initialize()

        st.title("📅 AI Revision Planner")

        st.write(
            "Generate a personalized AI-powered revision schedule."
        )

        st.divider()

        exam = st.text_input(
            "Exam Name"
        )

        subject = st.text_input(
            "Subject"
        )

        topics = st.text_area(

            "Topics",

            height=150,

            placeholder="Enter one or more topics..."

        )

        exam_date = st.date_input(
            "Exam Date"
        )

        hours = st.slider(

            "Study Hours Per Day",

            1,

            12,

            3

        )

        difficulty = st.selectbox(

            "Difficulty",

            DIFFICULTIES

        )

        goal = st.selectbox(

            "Goal",

            GOALS

        )

        plan_type = st.selectbox(

            "Plan Type",

            PLAN_TYPES

        )

        models = ModelService.get_models()

        model = st.selectbox(

            "AI Model",

            models

        )

        if st.button(

            "🚀 Generate Revision Plan",

            use_container_width=True

        ):

            if not exam.strip():

                st.warning("Please enter the exam name.")

                st.stop()

            if not subject.strip():

                st.warning("Please enter the subject.")

                st.stop()

            if not topics.strip():

                st.warning("Please enter the topics.")

                st.stop()

            try:

                with st.spinner(

                    "Generating Revision Plan..."

                ):

                    plan = RevisionPlannerService.generate(

                        exam,

                        subject,

                        topics,

                        exam_date,

                        hours,

                        difficulty,

                        goal,

                        plan_type,

                        model

                    )

                st.session_state.revision_plan = plan

                st.session_state.planner_requests += 1

                PlannerHistory.add(

                    exam,

                    subject

                )

            except Exception as e:

                ErrorHandler.handle(e)

                return

        if st.session_state.revision_plan:

            st.divider()

            st.subheader("📖 AI Revision Plan")

            st.markdown(

                st.session_state.revision_plan

            )

            PlannerExporter.download(

                st.session_state.revision_plan

            )

            PlannerAnalytics.render(

                st.session_state.revision_plan

            )

        st.divider()

        if st.checkbox(

            "Show Planner History"

        ):

            history = PlannerHistory.get()

            if history:

                for item in reversed(history):

                    st.write(

                        f"📚 {item['exam']} - {item['subject']}"

                    )

            else:

                st.info(

                    "No planner history available."

                )

        st.divider()

        if st.button(

            "🗑 Clear Planner",

            use_container_width=True

        ):

            st.session_state.revision_plan = ""

            st.session_state.planner_requests = 0

            st.rerun()