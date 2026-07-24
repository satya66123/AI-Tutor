from automation.database.base_repository import BaseRepository


class ScheduleRepository(BaseRepository):

    def save(self, schedule):

        sql = """
        INSERT INTO workflow_schedule
        (
            schedule_id,
            workflow_id,
            schedule_type,
            cron_expression,
            next_run,
            last_run,
            is_active
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """

        self.execute(
            sql,
            (
                schedule.schedule_id,
                schedule.workflow_id,
                schedule.schedule_type.value,
                schedule.cron_expression,
                schedule.next_run,
                schedule.last_run,
                schedule.is_active
            )
        )

    def update(self, schedule):

        sql = """
        UPDATE workflow_schedule
        SET
            next_run=%s,
            last_run=%s,
            is_active=%s
        WHERE schedule_id=%s
        """

        self.execute(
            sql,
            (
                schedule.next_run,
                schedule.last_run,
                schedule.is_active,
                schedule.schedule_id
            )
        )

    def find(self, schedule_id):

        sql = """
        SELECT *
        FROM workflow_schedule
        WHERE schedule_id=%s
        """

        return self.fetchone(sql, (schedule_id,))

    def find_active(self):

        sql = """
        SELECT *
        FROM workflow_schedule
        WHERE is_active=TRUE
        """

        return self.fetchall(sql)