import json
import uuid

from automation.workflow import Workflow
from automation.workflow_step import WorkflowStep
from automation.task import Task
from automation.task_registry import TaskRegistry


class WorkflowDeserializer:

    @staticmethod
    def deserialize(json_text: str) -> Workflow:
        """
        Deserialize a workflow from a JSON string.
        """

        try:

            data = json.loads(json_text)

        except json.JSONDecodeError as ex:

            raise ValueError(
                f"Invalid workflow JSON: {ex}"
            )

        workflow = Workflow(

            workflow_id=data.get(
                "workflow_id",
                str(uuid.uuid4())
            ),

            workflow_name=data.get(
                "workflow_name",
                "New Workflow"
            ),

            description=data.get(
                "description",
                ""
            )

        )

        for step_data in data.get("steps", []):

            task_type = step_data.get("task")

            if not task_type:
                continue

            task_cls = TaskRegistry.get(task_type)

            if task_cls is None:

                print(
                    f"Warning: Task '{task_type}' is not registered."
                )

                continue

            task = Task(

                task_id=step_data.get(
                    "task_id",
                    str(uuid.uuid4())
                ),

                task_name=step_data.get(
                    "task_name",
                    task_type.capitalize()
                ),

                task_type=task_type,

                input_data=step_data.get(
                    "input_data",
                    {}
                ),

                output_data=step_data.get(
                    "output_data",
                    None
                ),

                status=step_data.get(
                    "status"
                ),

                error=step_data.get(
                    "error"
                )

            )

            runner = task_cls(task)

            # Restore runner information if supported

            if hasattr(runner, "status"):

                runner.status = step_data.get(
                    "runner_status",
                    runner.status
                )

            if hasattr(runner, "start_time"):

                runner.start_time = step_data.get(
                    "start_time"
                )

            if hasattr(runner, "end_time"):

                runner.end_time = step_data.get(
                    "end_time"
                )

            if hasattr(runner, "error"):

                runner.error = step_data.get(
                    "runner_error"
                )

            step = WorkflowStep(

                id=step_data.get(
                    "id",
                    str(uuid.uuid4())
                ),

                task=runner,

                depends_on=step_data.get(
                    "depends_on",
                    []
                ),

                conditions=step_data.get(
                    "conditions",
                    []
                ),

                enabled=step_data.get(
                    "enabled",
                    True
                )

            )

            workflow.steps.append(step)

            workflow.tasks.append(runner)

        return workflow

    @classmethod
    def from_dict(cls, data: dict) -> Workflow:
        """
        Deserialize from a Python dictionary.
        """

        json_text = json.dumps(data)

        return cls.deserialize(json_text)

    @classmethod
    def load(cls, filename: str) -> Workflow:
        """
        Load a workflow from a JSON file.
        """

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                return cls.deserialize(
                    file.read()
                )

        except FileNotFoundError:

            raise FileNotFoundError(
                f"Workflow file '{filename}' not found."
            )

        except Exception as ex:

            raise RuntimeError(
                f"Unable to load workflow: {ex}"
            )