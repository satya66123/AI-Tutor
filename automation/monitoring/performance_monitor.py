class PerformanceMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def average_execution_time(self):

        repos = self.persistence.repositories()

        sql = """
        SELECT AVG(duration) average_time
        FROM workflow_execution
        """

        return repos.executions.fetchone(sql)

    def total_workflows(self):

        repos = self.persistence.repositories()

        sql = """
        SELECT COUNT(*) total
        FROM workflows
        """

        return repos.workflows.fetchone(sql)

    def completed_workflows(self):

        repos = self.persistence.repositories()

        sql = """
        SELECT COUNT(*) total
        FROM workflows
        WHERE status='COMPLETED'
        """

        return repos.workflows.fetchone(sql)

    def failed_workflows(self):

        repos = self.persistence.repositories()

        sql = """
        SELECT COUNT(*) total
        FROM workflows
        WHERE status='FAILED'
        """

        return repos.workflows.fetchone(sql)