from automation.ui.monitoring.report_generator import ReportGenerator


class ExportService:

    def __init__(self):

        self.generator = ReportGenerator()

    def export_workflows(
            self,
            workflows
    ):

        self.generator.workflow_report(
            workflows,
            "workflow_report.csv"
        )

    def export_executions(
            self,
            executions
    ):

        self.generator.execution_report(
            executions,
            "execution_report.xlsx"
        )