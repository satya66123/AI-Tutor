import pandas as pd
import streamlit as st

from automation.monitoring.log_monitor import LogMonitor


class LogsPage:

    def __init__(self, persistence):

        self.monitor = LogMonitor(
            persistence
        )

    def render(self, workflow_id):

        logs = self.monitor.workflow_logs(
            workflow_id
        )

        st.header("Workflow Logs")

        st.dataframe(
            pd.DataFrame(logs),
            use_container_width=True
        )