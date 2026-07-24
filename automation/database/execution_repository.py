from automation.database.base_repository import BaseRepository


class ExecutionRepository(BaseRepository):

    def save(self, execution):

        sql = """
        INSERT INTO workflow_execution
        (
            execution_id,
            workflow_id,
            started_at,
            completed_at,
            duration,
            status
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        self.execute(

            sql,

            (

                execution.execution_id,

                execution.workflow_id,

                execution.started_at,

                execution.completed_at,

                execution.duration,

                execution.status

            )

        )

    def update(self, execution):

        sql = """
        UPDATE workflow_execution

        SET

            completed_at=%s,

            duration=%s,

            status=%s

        WHERE execution_id=%s
        """

        self.execute(

            sql,

            (

                execution.completed_at,

                execution.duration,

                execution.status,

                execution.execution_id

            )

        )

    def find(self, execution_id):

        sql = """

        SELECT *

        FROM workflow_execution

        WHERE execution_id=%s

        """

        return self.fetchone(

            sql,

            (execution_id,)

        )

    def find_by_workflow(self, workflow_id):

        sql = """

        SELECT *

        FROM workflow_execution

        WHERE workflow_id=%s

        ORDER BY started_at DESC

        """

        return self.fetchall(

            sql,

            (workflow_id,)

        )