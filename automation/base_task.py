from abc import ABC, abstractmethod
from datetime import datetime

from automation.task import Task
from automation.task_status import TaskStatus
from automation.workflow_context import WorkflowContext
import time



class BaseTask(ABC):

    def __init__(self, task: Task, retry_policy=None):
        self.name = None
        self.task = task
        self.retry_policy = retry_policy

    def execute(self, context: WorkflowContext):

        self.task.status = TaskStatus.RUNNING
        self.task.started_at = datetime.now()
        start = time.perf_counter()

        try:

            result = self.run(context)

            if result is None:
                result = {}

            self.task.output_data = result
            elapsed = time.perf_counter() - start
            self.task.output_data["execution_time"] = elapsed

            self.task.status = TaskStatus.COMPLETED

        except Exception as ex:

            self.task.status = TaskStatus.FAILED
            self.task.error = str(ex)

        finally:

            self.task.completed_at = datetime.now()

        return self

    @abstractmethod
    def run(self, context: WorkflowContext):
        pass