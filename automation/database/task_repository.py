from automation.database.base_repository import BaseRepository


class TaskRepository(BaseRepository):

    def save(self, task, workflow_id):

        sql = """
        INSERT INTO workflow_tasks
        (
            task_id,
            workflow_id,
            task_name,
            task_type,
            status,
            retry_count,
            execution_time,
            started_at,
            completed_at,
            error
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        self.execute(

            sql,

            (

                task.task_id,

                workflow_id,

                task.task_name,

                task.task_type,

                task.status.value,

                task.retry_count,

                task.execution_time,

                task.started_at,

                task.completed_at,

                task.error

            )

        )

    def update(self, task):

        sql = """
        UPDATE workflow_tasks

        SET

            status=%s,

            retry_count=%s,

            execution_time=%s,

            started_at=%s,

            completed_at=%s,

            error=%s

        WHERE task_id=%s
        """

        self.execute(

            sql,

            (

                task.status.value,

                task.retry_count,

                task.execution_time,

                task.started_at,

                task.completed_at,

                task.error,

                task.task_id

            )

        )

    def find(self, task_id):

        sql = """

        SELECT *

        FROM workflow_tasks

        WHERE task_id=%s

        """

        return self.fetchone(

            sql,

            (task_id,)

        )

    def find_by_workflow(self, workflow_id):

        sql = """

        SELECT *

        FROM workflow_tasks

        WHERE workflow_id=%s

        ORDER BY started_at

        """

        return self.fetchall(

            sql,

            (workflow_id,)

        )