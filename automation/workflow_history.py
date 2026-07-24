class WorkflowHistory:

    def __init__(self):

        self.history = []

    def save(self, workflow):

        self.history.append(workflow)

    def get_all(self):

        return self.history

    def clear(self):

        self.history.clear()