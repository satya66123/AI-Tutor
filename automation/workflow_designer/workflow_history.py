from automation.workflow_history import WorkflowHistory


class WorkflowHistoryManager:

    def __init__(self):

        self.history = WorkflowHistory()

    def save(self, workflow):

        self.history.save(workflow)

    def get_all(self):

        return self.history.get_all()

    def clear(self):

        self.history.clear()

    def latest(self):

        workflows = self.history.get_all()

        if workflows:

            return workflows[-1]

        return None

    def count(self):

        return len(
            self.history.get_all()
        )