from automation.workflow_context import WorkflowContext
from automation.workflow_executor import WorkflowExecutor


class DesignerWorkflowExecutor:

    def __init__(self):

        self.executor = WorkflowExecutor()

    def execute(self, workflow):

        context = WorkflowContext(
            workflow.workflow_id
        )

        return self.executor.execute(
            workflow,
            context
        )