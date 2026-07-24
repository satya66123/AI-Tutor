import pandas as pd


class ReportGenerator:

    @staticmethod
    def workflow_report(
            workflows,
            filename
    ):

        df = pd.DataFrame(workflows)

        df.to_csv(
            filename,
            index=False
        )

    @staticmethod
    def execution_report(
            executions,
            filename
    ):

        df = pd.DataFrame(executions)

        df.to_excel(
            filename,
            index=False
        )