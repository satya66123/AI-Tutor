from automation.database.workflow_repository import WorkflowRepository
from automation.database.task_repository import TaskRepository
from automation.database.execution_repository import ExecutionRepository
from automation.database.schedule_repository import ScheduleRepository
from automation.database.log_repository import LogRepository


class RepositoryFactory:

    def __init__(self, connection):

        self.connection = connection

    @property
    def workflows(self):

        return WorkflowRepository(self.connection)

    @property
    def tasks(self):

        return TaskRepository(self.connection)

    @property
    def executions(self):

        return ExecutionRepository(self.connection)

    @property
    def schedules(self):

        return ScheduleRepository(self.connection)

    @property
    def logs(self):

        return LogRepository(self.connection)