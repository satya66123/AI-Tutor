from automation.database.base_repository import BaseRepository


class WorkflowRepository(BaseRepository):

    def save(self, workflow):

        sql = """
        INSERT INTO workflows
        (
            workflow_id,
            workflow_name,
            description,
            status,
            created_at,
            updated_at
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        self.execute(

            sql,

            (

                workflow.workflow_id,

                workflow.workflow_name,

                workflow.description,

                workflow.status.value,

                workflow.created_at,

                workflow.updated_at

            )

        )

    def find(self, workflow_id):

        sql = """

        SELECT *

        FROM workflows

        WHERE workflow_id=%s

        """

        return self.fetchone(

            sql,

            (workflow_id,)

        )

    def update(self, workflow):
        sql = """
        UPDATE workflows
        SET
            status=%s,
            updated_at=%s
        WHERE workflow_id=%s
        """

        self.execute(
            sql,
            (
                workflow.status.value,
                workflow.updated_at,
                workflow.workflow_id
            )
        )

    def find_all(self):
        sql = """
        SELECT *
        FROM workflows
        ORDER BY created_at DESC
        """

        return self.fetchall(sql)