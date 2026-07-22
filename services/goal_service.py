"""
AI Mentor Goal Service
"""

from database.db_manager import DBManager
from models.mentor_models import MentorGoal


class GoalService:

    @staticmethod
    def create(goal: MentorGoal):

        sql = """
        INSERT INTO mentor_goals
        (
            title,
            description,
            category,
            target_value,
            current_value,
            progress,
            priority,
            status,
            due_date
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        return DBManager.execute(

            sql,

            (
                goal.title,
                goal.description,
                goal.category,
                goal.target_value,
                goal.current_value,
                goal.progress,
                goal.priority,
                goal.status,
                goal.due_date
            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *
        FROM mentor_goals
        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def get(goal_id):

        sql = """
        SELECT *
        FROM mentor_goals
        WHERE id=%s
        """

        return DBManager.fetch_one(

            sql,

            (
                goal_id,
            )

        )

    @staticmethod
    def update(goal: MentorGoal):

        sql = """
        UPDATE mentor_goals
        SET

            title=%s,

            description=%s,

            category=%s,

            target_value=%s,

            current_value=%s,

            progress=%s,

            priority=%s,

            status=%s,

            due_date=%s

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (
                goal.title,
                goal.description,
                goal.category,
                goal.target_value,
                goal.current_value,
                goal.progress,
                goal.priority,
                goal.status,
                goal.due_date,
                goal.id
            )

        )

    @staticmethod
    def delete(goal_id):

        sql = """
        DELETE
        FROM mentor_goals
        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (
                goal_id,
            )

        )

    @staticmethod
    def mark_completed(goal_id):

        sql = """
        UPDATE mentor_goals

        SET

            status='Completed',

            progress=100

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (
                goal_id,
            )

        )

    @staticmethod
    def update_progress(goal_id, current_value):

        goal = GoalService.get(goal_id)

        if not goal:

            return False

        target = goal["target_value"]

        progress = 0

        if target > 0:

            progress = round((current_value / target) * 100, 2)

            if progress > 100:

                progress = 100

        sql = """
        UPDATE mentor_goals

        SET

            current_value=%s,

            progress=%s

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (
                current_value,
                progress,
                goal_id
            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total,

            SUM(status='Completed') completed,

            SUM(status='Pending') pending,

            SUM(status='In Progress') in_progress,

            AVG(progress) average_progress

        FROM mentor_goals
        """

        return DBManager.fetch_one(sql)