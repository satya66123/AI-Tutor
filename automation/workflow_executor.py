from automation.workflow_context import WorkflowContext
from automation.dependency_resolver import DependencyResolver
from automation.retry_executor import RetryExecutor


class WorkflowExecutor:

    @staticmethod
    def execute(workflow):

        context = WorkflowContext(
            workflow_id=workflow.workflow_id
        )

        if workflow.steps:

            context.variables.update(
                workflow.steps[0].task.task.input_data
            )

        completed = set()

        results = {}

        while len(completed) < len(workflow.steps):

            progress = False

            for step in workflow.steps:

                if step.id in completed:
                    continue

                if not step.enabled:
                    completed.add(step.id)
                    continue

                if DependencyResolver.ready(
                            step,
                            completed,
                            context
                    ):
                       continue

                runner = step.task

                finished = RetryExecutor.execute(
                    runner,
                    context
                )

                results[
                    finished.task.task_name
                ] = finished.task.output_data

                completed.add(step.id)

                progress = True

            if not progress:
                raise RuntimeError(
                    "Circular dependency detected."
                )

        workflow.results = results

        return workflow