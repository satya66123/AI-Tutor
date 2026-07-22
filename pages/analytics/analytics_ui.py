"""
Learning Analytics UI
"""

import streamlit as st

from pages.analytics.analytics_service import (
    LearningAnalyticsService
)


class LearningAnalyticsUI:

    @staticmethod
    def render():

        st.title("📈 Learning Analytics Dashboard")

        st.write(
            "Track your overall AI Tutor learning progress."
        )

        data = LearningAnalyticsService.get_data()

        st.divider()

        st.subheader("💬 AI Tutor")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Questions",
                data["questions"]
            )

        with c2:

            st.metric(
                "Responses",
                data["responses"]
            )

        st.divider()

        st.subheader("📝 Quiz")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Quizzes",
                data["quizzes"]
            )

        with c2:

            st.metric(
                "Average Score",
                data["quiz_score"]
            )

        st.divider()

        st.subheader("📚 Learning Modules")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Flashcards",
                data["flashcards"]
            )

        with c2:

            st.metric(
                "Notes",
                data["notes"]
            )

        with c3:

            st.metric(
                "PDFs",
                data["pdfs"]
            )

        c4, c5, c6 = st.columns(3)

        with c4:

            st.metric(
                "PDF Questions",
                data["pdf_questions"]
            )

        with c5:

            st.metric(
                "Coding Requests",
                data["coding"]
            )

        with c6:

            st.metric(
                "Revision Plans",
                data["planner"]
            )

        st.divider()

        total = (

            data["questions"] +
            data["quizzes"] +
            data["flashcards"] +
            data["notes"] +
            data["pdfs"] +
            data["coding"] +
            data["planner"]

        )

        st.success(

            f"🎯 Total Learning Activities : {total}"

        )