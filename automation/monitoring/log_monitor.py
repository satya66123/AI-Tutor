class LogMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def workflow_logs(self, workflow_id):

        repos = self.persistence.repositories()

        return repos.logs.find_by_workflow(workflow_id)

    def task_logs(self, task_id):

        repos = self.persistence.repositories()

        return repos.logs.find_by_task(task_id)