from automation.workflow_builder import WorkflowBuilder
from automation.workflow_executor import WorkflowExecutor
from automation.parallel_workflow_executor import ParallelWorkflowExecutor
from automation.workflow_history import WorkflowHistory
from automation.workflow_logger import WorkflowLogger
from automation.workflow_status import WorkflowStatus
from automation.workflow_validator import WorkflowValidator

from automation.database.persistence_service import PersistenceService
from automation.database.unit_of_work import UnitOfWork


class WorkflowEngine:

    def __init__(
            self,
            database_config,
            parallel=False
    ):

        self.parallel = parallel

        if parallel:
            self.executor = ParallelWorkflowExecutor()
        else:
            self.executor = WorkflowExecutor()

        self.validator = WorkflowValidator()
        self.logger = WorkflowLogger()
        self.history = WorkflowHistory()

        # Module 8
        self.persistence = PersistenceService(database_config)

    def run(
            self,
            workflow_name,
            template,
            input_data
    ):

        workflow = WorkflowBuilder.build(
            workflow_name,
            template,
            input_data
        )

        self.logger.workflow_started(workflow)

        self.validator.validate(workflow)

        workflow.status = WorkflowStatus.RUNNING

        connection = self.persistence.database.get_connection()

        with UnitOfWork(connection) as uow:

            # Save workflow
            uow.repositories.workflows.save(workflow)

            # Save tasks
            for task in workflow.tasks:
                uow.repositories.tasks.save(
                    task,
                    workflow.workflow_id
                )

            # Execute workflow
            workflow = self.executor.execute(workflow)

            workflow.status = WorkflowStatus.COMPLETED

            # Update workflow
            uow.repositories.workflows.update(workflow)

            # Update tasks
            for task in workflow.tasks:
                uow.repositories.tasks.update(task)

        self.logger.workflow_completed(workflow)

        self.history.save(workflow)

        return workflow