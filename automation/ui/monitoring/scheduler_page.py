import pandas as pd
import streamlit as st

from automation.monitoring.scheduler_monitor import SchedulerMonitor


class SchedulerPage:

    def __init__(self, persistence):

        self.monitor = SchedulerMonitor(
            persistence
        )

    def render(self):

        schedules = self.monitor.get_schedules()

        st.header("Scheduler")

        st.dataframe(
            pd.DataFrame(schedules),
            use_container_width=True
        )