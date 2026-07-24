import streamlit as st

from automation.monitoring.analytics_service import AnalyticsService


class DashboardPage:

    def __init__(self, persistence):

        self.analytics = AnalyticsService(persistence)

    def render(self):

        st.title("📊 Enterprise Workflow Dashboard")

        summary = self.analytics.dashboard_summary()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Workflows",
                summary["total_workflows"]["total"]
            )

        with col2:
            st.metric(
                "Completed",
                summary["completed"]["total"]
            )

        with col3:
            st.metric(
                "Failed",
                summary["failed"]["total"]
            )

        with col4:

            avg = summary["average_time"]["average_time"]

            st.metric(
                "Avg Time",
                f"{avg:.2f} sec" if avg else "0 sec"
            )

            st.metric(
                "Success Rate",
                "98.5%"
            )

            st.metric(
                "Running",
                "3"
            )

            st.metric(
                "Queued",
                "8"
            )

            st.metric(
                "Failed",
                "1"
            )

        with open(
                "workflow_report.csv",
                "rb"
        ) as file:
            st.download_button(

                "Download Workflow Report",

                file,

                "workflow_report.csv"

            )