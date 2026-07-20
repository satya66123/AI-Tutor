"""
Dashboard UI
"""

import streamlit as st

from pages.dashboard.dashboard_cards import DashboardCards
from pages.dashboard.dashboard_service import DashboardService
from utils.health_check import HealthCheck


class DashboardUI:

    @staticmethod
    def render():

        st.title("📊 Dashboard")

        st.write(
            "Welcome back! Here's a quick overview of your AI Tutor."
        )

        stats = DashboardService.get_statistics()

        DashboardCards.render(stats)

        st.divider()

        st.subheader("🚀 Quick Actions")

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                    "🎓 AI Tutor",
                    use_container_width=True
            ):
                st.session_state.page = "🎓 AI Tutor"
                st.rerun()

        with col2:

            if st.button(
                    "📚 Study Planner",
                    use_container_width=True
            ):
                st.session_state.page = "📚 Study Planner"
                st.rerun()

        with col3:

            if st.button(
                    "⚙ Settings",
                    use_container_width=True
            ):
                st.session_state.page = "⚙ Settings"
                st.rerun()


        health = HealthCheck.run()

        st.divider()

        st.subheader("🩺 Application Health")

        if health["provider"]:

            st.success("Provider Connected")

        else:

            st.error("Provider Not Available")