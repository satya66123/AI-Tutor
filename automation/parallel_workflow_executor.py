from concurrent.futures import ThreadPoolExecutor, as_completed

from automation.workflow_context import WorkflowContext
from automation.dependency_resolver import DependencyResolver


class ParallelWorkflowExecutor:

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def execute(self, workflow):

        context = WorkflowContext(workflow.workflow_id)

        if workflow.steps:
            context.variables.update(
                workflow.steps[0].task.task.input_data
            )

        completed = set()
        results = {}

        while len(completed) < len(workflow.steps):

            ready_steps = []

            for step in workflow.steps:

                if step.id in completed:
                    continue

                if not step.enabled:
                    completed.add(step.id)
                    continue

                if DependencyResolver.ready(step, completed):
                    ready_steps.append(step)

            if not ready_steps:
                raise RuntimeError(
                    "No executable steps found. Circular dependency?"
                )

            with ThreadPoolExecutor(
                    max_workers=self.max_workers
            ) as executor:

                futures = {
                    executor.submit(
                        step.task.execute,
                        context
                    ): step
                    for step in ready_steps
                }

                for future in as_completed(futures):

                    step = futures[future]

                    runner = future.result()

                    results[
                        runner.task.task_name
                    ] = runner.task.output_data

                    completed.add(step.id)

        workflow.results = results

        return workflow