import json
import streamlit as st

from automation.workflow_designer.workflow_serializer import WorkflowSerializer
from automation.workflow_designer.workflow_deserializer import WorkflowDeserializer


class ImportExportPanel:

    def __init__(self):

        self.serializer = WorkflowSerializer()

        self.deserializer = WorkflowDeserializer()

    def render(self, workflow):

        st.subheader("Import / Export")

        col1, col2 = st.columns(2)

        # --------------------------
        # Export
        # --------------------------

        with col1:

            st.markdown("### Export Workflow")

            filename = st.text_input(
                "File Name",
                value="workflow.json",
                key="export_filename"
            )

            if st.button(
                "Export",
                use_container_width=True
            ):

                try:

                    data = self.serializer.to_dict(workflow)

                    json_text = json.dumps(
                        data,
                        indent=4
                    )

                    st.download_button(

                        label="Download Workflow",

                        data=json_text,

                        file_name=filename,

                        mime="application/json",

                        use_container_width=True

                    )

                except Exception as ex:

                    st.error(str(ex))

        # --------------------------
        # Import
        # --------------------------

        with col2:

            st.markdown("### Import Workflow")

            uploaded = st.file_uploader(

                "Choose Workflow",

                type=["json"]

            )

            if uploaded is not None:

                try:

                    data = json.load(uploaded)

                    workflow = self.deserializer.from_dict(
                        data
                    )

                    st.success(
                        "Workflow imported successfully."
                    )

                    return workflow

                except Exception as ex:

                    st.error(str(ex))

        return None