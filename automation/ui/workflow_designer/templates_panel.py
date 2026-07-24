import streamlit as st

from automation.workflow_designer.template_manager import TemplateManager


class TemplatesPanel:

    def __init__(self):

        self.manager = TemplateManager()

    def render(self):

        st.subheader("Workflow Templates")

        templates = self.manager.list_templates()

        if not templates:

            st.info("No templates available.")

            return None

        selected = st.selectbox(

            "Select Template",

            templates

        )

        col1, col2 = st.columns(2)

        with col1:

            load = st.button(

                "Load Template",

                use_container_width=True

            )

        with col2:

            preview = st.button(

                "Preview",

                use_container_width=True

            )

        if preview:

            try:

                template = self.manager.load_template(

                    selected

                )

                st.json(template)

            except Exception as ex:

                st.error(str(ex))

        if load:

            try:

                workflow = self.manager.create_workflow(

                    selected

                )

                st.success(

                    f"{selected} template loaded."

                )

                return workflow

            except Exception as ex:

                st.error(str(ex))

        return None