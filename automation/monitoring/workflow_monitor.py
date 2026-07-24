class WorkflowMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def get_workflows(self):

        repos = self.persistence.repositories()

        return repos.workflows.find_all()

    def get_workflow(self, workflow_id):

        repos = self.persistence.repositories()

        return repos.workflows.find(workflow_id)