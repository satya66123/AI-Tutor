from automation.database.base_repository import BaseRepository


class LogRepository(BaseRepository):

    def save(self, log):

        sql = """
        INSERT INTO workflow_logs
        (
            log_id,
            workflow_id,
            task_id,
            log_level,
            message,
            created_at
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        self.execute(
            sql,
            (
                log.log_id,
                log.workflow_id,
                log.task_id,
                log.log_level,
                log.message,
                log.created_at
            )
        )

    def find_by_workflow(self, workflow_id):

        sql = """
        SELECT *
        FROM workflow_logs
        WHERE workflow_id=%s
        ORDER BY created_at DESC
        """

        return self.fetchall(sql, (workflow_id,))

    def find_by_task(self, task_id):

        sql = """
        SELECT *
        FROM workflow_logs
        WHERE task_id=%s
        ORDER BY created_at DESC
        """

        return self.fetchall(sql, (task_id,))

    def delete_old_logs(self, before_date):

        sql = """
        DELETE
        FROM workflow_logs
        WHERE created_at < %s
        """

        self.execute(sql, (before_date,))