from automation.workflow import Workflow


class WorkflowValidator:

    @staticmethod
    def validate(workflow: Workflow):

        if workflow is None:
            raise ValueError("Workflow cannot be None")

        if not workflow.tasks:
            raise ValueError("Workflow has no tasks")

        return True