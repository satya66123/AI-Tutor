import pandas as pd
import plotly.express as px
import streamlit as st


class DashboardCharts:

    @staticmethod
    def workflow_status_chart(workflows):

        df = pd.DataFrame(workflows)

        if df.empty:
            st.info("No workflow data available.")
            return

        counts = df["status"].value_counts().reset_index()
        counts.columns = ["Status", "Count"]

        fig = px.pie(
            counts,
            values="Count",
            names="Status",
            title="Workflow Status Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def execution_time_chart(executions):

        df = pd.DataFrame(executions)

        if df.empty:
            st.info("No execution data available.")
            return

        fig = px.bar(
            df,
            x="execution_id",
            y="duration",
            title="Workflow Execution Time"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def retry_chart(tasks):

        df = pd.DataFrame(tasks)

        if df.empty:
            st.info("No task data available.")
            return

        fig = px.bar(
            df,
            x="task_name",
            y="retry_count",
            title="Task Retry Count"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )