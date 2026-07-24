import logging

logging.basicConfig(level=logging.INFO)


class WorkflowLogger:

    @staticmethod
    def workflow_started(workflow):

        logging.info(
            f"Workflow Started : {workflow.workflow_name}"
        )

    @staticmethod
    def workflow_completed(workflow):

        logging.info(
            f"Workflow Completed : {workflow.workflow_name}"
        )

    @staticmethod
    def workflow_failed(workflow, error):

        logging.error(

            f"{workflow.workflow_name} Failed : {error}"

        )