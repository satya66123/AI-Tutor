import uuid

from automation.task import Task
from automation.task_registry import TaskRegistry
from automation.workflow_step import WorkflowStep


class DesignerService:

    @staticmethod
    def add_step(

            workflow,

            task_name,

            input_data=None

    ):

        if input_data is None:

            input_data = {}

        task_class = TaskRegistry.get(task_name)

        if task_class is None:

            raise ValueError(

                f"Unknown task '{task_name}'"

            )

        task = Task(

            task_id=str(uuid.uuid4()),

            task_name=task_name.capitalize(),

            task_type=task_name,

            input_data=input_data

        )

        runner = task_class(task)

        step = WorkflowStep(

            id=task.task_id,

            task=runner

        )

        if workflow.steps:

            step.depends_on.append(

                workflow.steps[-1].id

            )

        workflow.steps.append(step)

        workflow.tasks.append(runner)

        return step