import pandas as pd
import streamlit as st

from automation.monitoring.workflow_monitor import WorkflowMonitor


class WorkflowPage:

    def __init__(self, persistence):

        self.monitor = WorkflowMonitor(persistence)

    def render(self):

        st.header("Workflows")

        workflows = self.monitor.get_workflows()

        df = pd.DataFrame(workflows)

        st.dataframe(
            df,
            use_container_width=True
        )