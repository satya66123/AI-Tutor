import uuid

from automation.task import Task
from automation.workflow import Workflow
from automation.workflow_step import WorkflowStep
from automation.task_registry import TaskRegistry


class WorkflowBuilder:

    @staticmethod
    def build(workflow_name, template, input_data):

        steps = []

        previous = None

        for task_name in template:

            task_cls = TaskRegistry.get(task_name)

            task = Task(
                task_id=str(uuid.uuid4()),
                task_name=task_name.capitalize(),
                task_type=task_name,
                input_data=input_data.copy()
            )

            runner = task_cls(task)

            step = WorkflowStep(
                id=task.task_id,
                task=runner
            )

            if previous:
                step.depends_on.append(previous)

            previous = step.id

            steps.append(step)

        return Workflow(
            workflow_id=str(uuid.uuid4()),
            workflow_name=workflow_name,
            description=workflow_name,
            steps=steps
        )