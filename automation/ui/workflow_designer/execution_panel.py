import time
import streamlit as st


class ExecutionPanel:

    def __init__(self, executor):

        self.executor = executor

    @staticmethod
    def render(workflow):

        st.subheader("Workflow Execution")

        if workflow is None:

            st.warning("No workflow available.")

            return

        total_steps = len(workflow.steps)

        if total_steps == 0:

            st.info("Workflow contains no steps.")

            return

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Steps",
                total_steps
            )

        completed = len([
            step
            for step in workflow.steps
            if step.task.status.name == "COMPLETED"
        ])

        with col2:

            st.metric(
                "Completed",
                completed
            )

        pending = total_steps - completed

        with col3:

            st.metric(
                "Pending",
                pending
            )

        st.divider()

        progress_placeholder = st.empty()

        log_placeholder = st.empty()

        status_placeholder = st.empty()

        if st.button(
                "▶ Execute Workflow",
                use_container_width=True
        ):

            progress = progress_placeholder.progress(0)

            logs = []

            for index, step in enumerate(workflow.steps):

                status_placeholder.info(

                    f"Executing : {step.task.task.task_name}"

                )

                try:

                    result = step.task.execute({})

                    logs.append(

                        f"✔ {step.task.task.task_name}"

                    )

                except Exception as ex:

                    logs.append(

                        f"✘ {step.task.task.task_name} : {ex}"

                    )

                progress.progress(

                    int((index + 1) / total_steps * 100)

                )

                log_placeholder.code(

                    "\n".join(logs),

                    language="text"

                )

                time.sleep(0.2)

            status_placeholder.success(

                "Workflow Execution Completed"

            )

        st.divider()

        st.subheader("Workflow Steps")

        for i, step in enumerate(workflow.steps):

            with st.expander(

                f"Step {i + 1} : {step.task.task.task_name}",

                expanded=False

            ):

                st.write("Step ID")

                st.code(step.id)

                st.write("Task Type")

                st.code(step.task.task.task_type)

                st.write("Dependencies")

                st.write(step.depends_on)

                st.write("Enabled")

                st.write(step.enabled)

                st.write("Status")

                st.write(step.task.status.name)

                st.write("Error")

                st.write(step.task.error)

                st.write("Input")

                st.code(str(step.task.task.input_data))

                st.write("Output")

                st.code(str(step.task.task.output_data))