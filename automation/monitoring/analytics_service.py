from automation.monitoring.performance_monitor import PerformanceMonitor
from automation.monitoring.workflow_monitor import WorkflowMonitor
from automation.monitoring.task_monitor import TaskMonitor


class AnalyticsService:

    def __init__(self, persistence):

        self.workflow = WorkflowMonitor(persistence)

        self.task = TaskMonitor(persistence)

        self.performance = PerformanceMonitor(persistence)

    def dashboard_summary(self):

        return {

            "total_workflows":
                self.performance.total_workflows(),

            "completed":
                self.performance.completed_workflows(),

            "failed":
                self.performance.failed_workflows(),

            "average_time":
                self.performance.average_execution_time()

        }