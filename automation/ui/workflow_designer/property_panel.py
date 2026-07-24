import streamlit as st


class PropertyPanel:

    @staticmethod
    def render(workflow):

        st.subheader("Workflow Properties")

        workflow.workflow_name = st.text_input(
            "Workflow Name",
            workflow.workflow_name
        )

        workflow.description = st.text_area(
            "Description",
            workflow.description
        )

        st.metric(
            "Steps",
            len(workflow.steps)
        )

        st.metric(
            "Tasks",
            len(workflow.tasks)
        )

        st.metric(
            "Status",
            workflow.status.name
        )