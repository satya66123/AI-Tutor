class ExecutionMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def get_executions(self, workflow_id):

        repos = self.persistence.repositories()

        return repos.executions.find_by_workflow(workflow_id)