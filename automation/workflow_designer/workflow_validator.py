class WorkflowValidator:

    @staticmethod
    def validate(workflow):

        errors = []

        if not workflow.workflow_name.strip():

            errors.append(
                "Workflow name is required."
            )

        if len(workflow.steps) == 0:

            errors.append(
                "Workflow must contain at least one step."
            )

        ids = set()

        for step in workflow.steps:

            if step.id in ids:

                errors.append(
                    f"Duplicate Step ID : {step.id}"
                )

            ids.add(step.id)

        return errors

    def is_valid(self, workflow):

        return len(self.validate(workflow)) == 0