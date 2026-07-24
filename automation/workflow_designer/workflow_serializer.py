import json


class WorkflowSerializer:

    @staticmethod
    def serialize(
            workflow
    ):

        data = {

            "workflow_id":
                workflow.workflow_id,

            "workflow_name":
                workflow.workflow_name,

            "description":
                workflow.description,

            "status":
                workflow.status.name,

            "steps": [

                {

                    "id": step.id,

                    "task":

                        step.task.task.task_type,

                    "depends_on":

                        step.depends_on,

                    "enabled":

                        step.enabled

                }

                for step in workflow.steps

            ]

        }

        return json.dumps(
            data,
            indent=4
        )

    def save(
            self,
            workflow,
            filename
    ):

        text = self.serialize(
            workflow
        )

        with open(
                filename,
                "w",
                encoding="utf-8"
        ) as file:

            file.write(text)

    @staticmethod
    def to_dict(workflow):
        return {

            "workflow_id": workflow.workflow_id,

            "workflow_name": workflow.workflow_name,

            "description": workflow.description,

            "steps": [

                {

                    "id": step.id,

                    "task_type": step.task.task.task_type,

                    "depends_on": step.depends_on,

                    "enabled": step.enabled

                }

                for step in workflow.steps

            ]

        }