import json
from pathlib import Path


class TemplateManager:

    def __init__(self):

        self.template_dir = Path(
            "automation/workflow_designer/templates"
        )

        self.template_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(
            self,
            workflow,
            filename
    ):

        path = self.template_dir / filename

        data = {

            "workflow_name":
                workflow.workflow_name,

            "description":
                workflow.description,

            "steps": [

                {

                    "task":
                        step.task.task.task_type,

                    "depends_on":
                        step.depends_on

                }

                for step in workflow.steps

            ]

        }

        with open(
                path,
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def list_templates(self):

        return [

            file.name

            for file in self.template_dir.glob(
                "*.json"
            )

        ]

    def load(self, filename):

        path = self.template_dir / filename

        with open(
                path,
                "r",
                encoding="utf-8"
        ) as file:

            return json.load(file)

    def load_template(self, selected):
        pass

    def create_workflow(self, selected):
        pass