import streamlit as st


class WorkflowHistoryPage:

    @staticmethod
    def render():

        st.subheader("📜 Workflow History")

        history = st.session_state.get("workflow_history")

        if history is None:
            st.warning("Workflow History Manager not initialized.")
            return

        try:
            workflows = history.get_all()
        except Exception as ex:
            st.error(f"Failed to load workflow history: {ex}")
            return

        if not workflows:
            st.info("No workflow history found.")
            return

        for workflow in workflows:

            with st.expander(
                workflow.workflow_name,
                expanded=False
            ):

                st.write("### Workflow Information")

                st.write({
                    "Workflow ID": workflow.workflow_id,
                    "Workflow Name": workflow.workflow_name,
                    "Description": workflow.description,
                    "Status": workflow.status.name if hasattr(workflow.status, "name") else workflow.status,
                    "Steps": len(workflow.steps)
                })

                if hasattr(workflow, "tasks") and workflow.tasks:

                    st.write("### Tasks")

                    for task in workflow.tasks:

                        st.write({
                            "Task ID": getattr(task, "task_id", ""),
                            "Task Name": getattr(task, "task_name", ""),
                            "Task Type": getattr(task, "task_type", ""),
                            "Status": getattr(task, "status", "")
                        })