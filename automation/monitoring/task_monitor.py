class TaskMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def get_tasks(self, workflow_id):

        repos = self.persistence.repositories()

        return repos.tasks.find_by_workflow(workflow_id)