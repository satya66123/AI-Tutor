import streamlit as st


class StepEditor:
    """
    Enterprise Workflow Step Editor
    """

    @staticmethod
    def render(workflow):

        st.subheader("Step Editor")

        if workflow is None:
            st.info("No workflow loaded.")
            return

        if len(workflow.steps) == 0:
            st.info("No workflow steps available.")
            return

        # -----------------------------
        # Step Selection
        # -----------------------------

        step_ids = [step.id for step in workflow.steps]

        default_index = 0

        if "selected_step" in st.session_state:

            if st.session_state.selected_step in step_ids:

                default_index = step_ids.index(
                    st.session_state.selected_step
                )

        selected_id = st.selectbox(
            "Select Step",
            step_ids,
            index=default_index
        )

        st.session_state.selected_step = selected_id

        step = next(
            s for s in workflow.steps
            if s.id == selected_id
        )

        task_runner = step.task
        task = task_runner.task

        st.divider()

        # ====================================================
        # STEP INFORMATION
        # ====================================================

        st.markdown("## Step")

        col1, col2 = st.columns(2)

        with col1:

            step.id = st.text_input(
                "Step ID",
                value=step.id
            )

        with col2:

            step.enabled = st.checkbox(
                "Enabled",
                value=step.enabled
            )

        st.divider()

        # ====================================================
        # TASK INFORMATION
        # ====================================================

        st.markdown("## Task")

        task.task_name = st.text_input(
            "Task Name",
            value=task.task_name
        )

        st.text_input(
            "Task Type",
            value=task.task_type,
            disabled=True
        )

        st.text_area(
            "Input Data",
            value=str(task.input_data)
        )

        st.text_area(
            "Output Data",
            value=str(task.output_data),
            disabled=True,
            height=120
        )

        st.divider()

        # ====================================================
        # DEPENDENCIES
        # ====================================================

        st.markdown("## Dependencies")

        available = []

        for s in workflow.steps:

            if s.id != step.id:

                available.append(s.id)

        step.depends_on = st.multiselect(
            "Depends On",
            available,
            default=step.depends_on
        )

        st.divider()

        # ====================================================
        # CONDITIONS
        # ====================================================

        st.markdown("## Conditions")

        if len(step.conditions) == 0:

            st.info("No conditions configured.")

        else:

            for index, condition in enumerate(step.conditions):

                st.write(
                    f"{index+1}. {condition}"
                )

        st.divider()

        # ====================================================
        # EXECUTION
        # ====================================================

        st.markdown("## Execution")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Status",
                str(task_runner.status.name)
            )

        with c2:

            st.metric(
                "Enabled",
                str(step.enabled)
            )

        c3, c4 = st.columns(2)

        with c3:

            st.text_input(
                "Started",
                value=str(task_runner.start_time),
                disabled=True
            )

        with c4:

            st.text_input(
                "Finished",
                value=str(task_runner.end_time),
                disabled=True
            )

        st.divider()

        # ====================================================
        # ERROR
        # ====================================================

        st.markdown("## Error")

        st.text_area(
            "Execution Error",
            value=str(task_runner.error),
            disabled=True,
            height=120
        )

        st.divider()

        # ====================================================
        # BUTTONS
        # ====================================================

        c1, c2, c3 = st.columns(3)

        with c1:

            if st.button(
                "Save Changes",
                use_container_width=True
            ):

                st.success(
                    "Step updated successfully."
                )

        with c2:

            if st.button(
                "Reset",
                use_container_width=True
            ):

                st.rerun()

        with c3:

            if st.button(
                "Delete Step",
                use_container_width=True
            ):

                workflow.steps.remove(step)

                if task_runner in workflow.tasks:
                    workflow.tasks.remove(task_runner)

                st.success(
                    "Step deleted."
                )

                st.rerun()