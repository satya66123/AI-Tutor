from automation.base_task import BaseTask


class AnalyticsTask(BaseTask):

    def run(self, context):

        document = context.get("document")

        analytics = f"Generated Analytics for {document}"

        context.set("analytics", analytics)

        return {
            "analytics": analytics
        }