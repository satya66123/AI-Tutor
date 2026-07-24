import streamlit as st

from automation.workflow_designer.designer import WorkflowDesigner
from automation.workflow_designer.designer_service import DesignerService
from automation.workflow_designer.workflow_serializer import WorkflowSerializer
from automation.workflow_designer.workflow_deserializer import WorkflowDeserializer
from automation.workflow_designer.workflow_executor import DesignerWorkflowExecutor
from automation.workflow_designer.workflow_history import WorkflowHistoryManager
from automation.ui.workflow_designer.step_editor import StepEditor
from automation.ui.workflow_designer.execution_panel import ExecutionPanel
from automation.ui.workflow_designer.templates_panel import TemplatesPanel
from automation.ui.workflow_designer.import_export_panel import ImportExportPanel
from automation.ui.workflow_designer.keyboard_shortcuts import KeyboardShortcuts
from automation.ui.workflow_designer.workflow_statistics import WorkflowStatistics

from automation.ui.workflow_designer.toolbar import Toolbar
from automation.ui.workflow_designer.task_palette import TaskPalette
from automation.ui.workflow_designer.canvas import Canvas
from automation.ui.workflow_designer.property_panel import PropertyPanel
from automation.ui.workflow_designer.workflow_history_page import WorkflowHistoryPage
from automation.ui.workflow_designer.validation_panel import ValidationPanel


class WorkflowDesignerPage:

    @staticmethod
    def render():
        page = WorkflowDesignerPage()
        page._render()

    def __init__(self):

        if "workflow_designer" not in st.session_state:
            st.session_state.workflow_designer = WorkflowDesigner()

        if "designer_service" not in st.session_state:
            st.session_state.designer_service = DesignerService()

        if "workflow_serializer" not in st.session_state:
            st.session_state.workflow_serializer = WorkflowSerializer()

        if "workflow_deserializer" not in st.session_state:
            st.session_state.workflow_deserializer = WorkflowDeserializer()

        if "workflow_executor" not in st.session_state:
            st.session_state.workflow_executor = DesignerWorkflowExecutor()

        if "workflow_history" not in st.session_state:
            st.session_state.workflow_history = WorkflowHistoryManager()

        self.designer = st.session_state.workflow_designer
        self.shortcuts = KeyboardShortcuts()
        self.step_editor = StepEditor()
        self.service = st.session_state.designer_service
        self.serializer = st.session_state.workflow_serializer
        self.deserializer = st.session_state.workflow_deserializer
        self.executor = st.session_state.workflow_executor
        self.history = st.session_state.workflow_history

        self.toolbar = Toolbar()
        self.templates = TemplatesPanel()
        self.execution = ExecutionPanel(self.executor)
        self.palette = TaskPalette()
        self.canvas = Canvas()
        self.validation = ValidationPanel()
        self.properties = PropertyPanel()
        self.history_page = WorkflowHistoryPage()
        self.import_export = ImportExportPanel()
        self.statistics = WorkflowStatistics()

    def _render(self):

        st.title("Workflow Designer")

        workflow = self.designer.get_workflow()

        actions = self.toolbar.render()

        if actions["new"]:
            self.designer.new(
                workflow_name="New Workflow",
                description=""
            )
            st.success("New workflow created.")
            st.rerun()

        if actions["clear"]:
            self.designer.clear()
            st.success("Workflow cleared.")
            st.rerun()

        if actions["save"]:
            try:
                self.serializer.save(workflow, "workflow.json")
                st.success("Workflow saved.")
            except Exception as ex:
                st.error(str(ex))

        if actions["execute"]:
            try:
                result = self.executor.execute(workflow)
                self.history.save(result)
                st.success("Workflow executed successfully.")
            except Exception as ex:
                st.error(str(ex))

        col1, col2 = st.columns([1, 5])

        with col1:
            if st.button("Load Workflow", use_container_width=True):
                try:
                    loaded = self.deserializer.load("workflow.json")
                    self.designer.workflow = loaded
                    st.success("Workflow loaded.")
                    st.rerun()
                except Exception as ex:
                    st.error(str(ex))

        st.divider()

        self.properties.render(workflow)

        st.divider()

        selected_task, add = self.palette.render()

        if add:
            try:
                self.service.add_step(workflow, selected_task)
                st.success(f"{selected_task} added.")
                st.rerun()
            except Exception as ex:
                st.error(str(ex))

        st.divider()

        loaded_workflow = self.templates.render()

        if loaded_workflow is not None:
            self.designer.workflow = loaded_workflow
            st.success("Workflow loaded from template.")
            st.rerun()

        st.divider()

        loaded = self.import_export.render(workflow)

        if loaded is not None:
            self.designer.workflow = loaded
            st.success("Workflow imported.")
            st.rerun()

        st.divider()

        self.canvas.render(workflow)

        st.divider()

        self.step_editor.render(workflow)

        st.divider()

        self.history_page.render()

        st.divider()

        self.validation.render(workflow)

        st.divider()

        self.execution.render(workflow)

        st.divider()

        self.shortcuts.render()

        st.divider()

        self.statistics.render(workflow)