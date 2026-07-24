from automation.plugins.plugin import Plugin


class PlannerPlugin(Plugin):

    def __init__(self):

        super().__init__()

        self.name = "Planner Plugin"

    def initialize(self):

        print("Planner Ready")

    def execute(
            self,
            context
    ):

        return {

            "plan":

                context.get("goal")

        }

    def shutdown(self):

        print("Planner Closed")