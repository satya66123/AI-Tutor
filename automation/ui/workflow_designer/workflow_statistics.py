import streamlit as st


class WorkflowStatistics:

    @staticmethod
    def render(workflow):

        st.subheader("Workflow Statistics")

        if workflow is None:

            return

        total = len(workflow.steps)

        enabled = len(
            [
                s
                for s in workflow.steps
                if s.enabled
            ]
        )

        disabled = total - enabled

        dependencies = sum(
            len(step.depends_on)
            for step in workflow.steps
        )

        conditions = sum(
            len(step.conditions)
            for step in workflow.steps
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Steps",
            total
        )

        c2.metric(
            "Enabled",
            enabled
        )

        c3.metric(
            "Dependencies",
            dependencies
        )

        c4.metric(
            "Conditions",
            conditions
        )

        completed = 0

        failed = 0

        pending = 0

        for step in workflow.steps:

            try:

                status = step.task.status.name

                if status == "COMPLETED":

                    completed += 1

                elif status == "FAILED":

                    failed += 1

                else:

                    pending += 1

            except Exception:

                pending += 1

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Completed",
            completed
        )

        c2.metric(
            "Failed",
            failed
        )

        c3.metric(
            "Pending",
            pending
        )

        progress = 0

        if total > 0:

            progress = completed / total

        st.progress(progress)