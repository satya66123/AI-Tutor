import uuid

from automation.workflow import Workflow
from automation.workflow_status import WorkflowStatus
from automation.workflow_step import WorkflowStep


class WorkflowDesigner:

    def __init__(self):

        self.workflow = Workflow(
            workflow_id=str(uuid.uuid4()),
            workflow_name="New Workflow",
            description=""
        )

    def new(
            self,
            workflow_name: str,
            description: str = ""
    ):

        self.workflow = Workflow(
            workflow_id=str(uuid.uuid4()),
            workflow_name=workflow_name,
            description=description
        )

        return self.workflow

    def add_step(
            self,
            step: WorkflowStep
    ):

        self.workflow.steps.append(step)

        self.workflow.tasks.append(step.task)

    def remove_step(
            self,
            step_id: str
    ):

        steps = []

        tasks = []

        for step in self.workflow.steps:

            if step.id != step_id:
                steps.append(step)
                tasks.append(step.task)

        self.workflow.steps = steps
        self.workflow.tasks = tasks

    def get_step(
            self,
            step_id: str
    ):

        for step in self.workflow.steps:

            if step.id == step_id:
                return step

        return None

    def clear(self):

        self.workflow.steps.clear()
        self.workflow.tasks.clear()
        self.workflow.results.clear()

        self.workflow.status = WorkflowStatus.PENDING

    def rename(
            self,
            workflow_name: str
    ):

        self.workflow.workflow_name = workflow_name

    def description(
            self,
            description: str
    ):

        self.workflow.description = description

    def get_workflow(self):

        return self.workflow