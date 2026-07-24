import streamlit as st


class Canvas:

    @staticmethod
    def render(workflow):

        st.subheader("Workflow Canvas")

        if workflow is None:

            st.warning("Workflow not available.")

            return

        if len(workflow.steps) == 0:

            st.info("No workflow steps.")

            return

        for index, step in enumerate(workflow.steps):

            with st.container():

                c1, c2, c3, c4, c5 = st.columns(
                    [4, 1, 1, 1, 1]
                )

                with c1:

                    st.markdown(
                        f"### {index + 1}. {step.task.task.task_name}"
                    )

                    st.caption(
                        f"ID : {step.id}"
                    )

                    st.write(
                        f"Type : {step.task.task.task_type}"
                    )

                    st.write(
                        f"Depends On : {step.depends_on}"
                    )

                with c2:

                    if st.button(
                        "⬆",
                        key=f"up_{step.id}",
                        use_container_width=True
                    ):

                        if index > 0:

                            workflow.steps[index], workflow.steps[index - 1] = (

                                workflow.steps[index - 1],

                                workflow.steps[index]

                            )

                            workflow.tasks[index], workflow.tasks[index - 1] = (

                                workflow.tasks[index - 1],

                                workflow.tasks[index]

                            )

                            st.rerun()

                with c3:

                    if st.button(
                        "⬇",
                        key=f"down_{step.id}",
                        use_container_width=True
                    ):

                        if index < len(workflow.steps) - 1:

                            workflow.steps[index], workflow.steps[index + 1] = (

                                workflow.steps[index + 1],

                                workflow.steps[index]

                            )

                            workflow.tasks[index], workflow.tasks[index + 1] = (

                                workflow.tasks[index + 1],

                                workflow.tasks[index]

                            )

                            st.rerun()

                with c4:

                    if st.button(
                        "✏",
                        key=f"edit_{step.id}",
                        use_container_width=True
                    ):

                        st.session_state.selected_step = step.id

                        st.rerun()

                with c5:

                    if st.button(
                        "🗑",
                        key=f"delete_{step.id}",
                        use_container_width=True
                    ):

                        workflow.steps.remove(step)

                        if step.task in workflow.tasks:

                            workflow.tasks.remove(step.task)

                        st.rerun()

                st.divider()