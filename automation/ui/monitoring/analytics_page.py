import streamlit as st

from automation.monitoring.performance_monitor import PerformanceMonitor


class AnalyticsPage:

    def __init__(self, persistence):

        self.performance = PerformanceMonitor(
            persistence
        )

    def render(self):

        st.header("Performance")

        st.json({

            "Average Time":
                self.performance.average_execution_time(),

            "Total Workflows":
                self.performance.total_workflows(),

            "Completed":
                self.performance.completed_workflows(),

            "Failed":
                self.performance.failed_workflows()

        })