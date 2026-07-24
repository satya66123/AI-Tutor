import pandas as pd
import streamlit as st

from automation.monitoring.execution_monitor import ExecutionMonitor


class ExecutionPage:

    def __init__(self, persistence):

        self.monitor = ExecutionMonitor(persistence)

    def render(self, workflow_id):

        executions = self.monitor.get_executions(
            workflow_id
        )

        st.subheader("Execution History")

        st.dataframe(
            pd.DataFrame(executions),
            use_container_width=True
        )