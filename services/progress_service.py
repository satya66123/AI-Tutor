"""
AI Mentor Progress Service
"""

from database.db_manager import DBManager
from models.mentor_models import MentorProgress


class ProgressService:

    @staticmethod
    def create(progress: MentorProgress):

        sql = """
        INSERT INTO mentor_progress
        (
            study_date,
            study_hours,
            quizzes_completed,
            flashcards_completed,
            notes_created,
            coding_sessions,
            rag_queries,
            score,
            remarks
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        return DBManager.execute(

            sql,

            (

                progress.study_date,

                progress.study_hours,

                progress.quizzes_completed,

                progress.flashcards_completed,

                progress.notes_created,

                progress.coding_sessions,

                progress.rag_queries,

                progress.score,

                progress.remarks

            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *
        FROM mentor_progress
        ORDER BY study_date DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def get(progress_id):

        sql = """
        SELECT *
        FROM mentor_progress
        WHERE id=%s
        """

        return DBManager.fetch_one(

            sql,

            (

                progress_id,

            )

        )

    @staticmethod
    def update(progress: MentorProgress):

        sql = """
        UPDATE mentor_progress
        SET

            study_date=%s,

            study_hours=%s,

            quizzes_completed=%s,

            flashcards_completed=%s,

            notes_created=%s,

            coding_sessions=%s,

            rag_queries=%s,

            score=%s,

            remarks=%s

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                progress.study_date,

                progress.study_hours,

                progress.quizzes_completed,

                progress.flashcards_completed,

                progress.notes_created,

                progress.coding_sessions,

                progress.rag_queries,

                progress.score,

                progress.remarks,

                progress.id

            )

        )

    @staticmethod
    def delete(progress_id):

        sql = """
        DELETE
        FROM mentor_progress
        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                progress_id,

            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_sessions,

            SUM(study_hours) total_hours,

            AVG(study_hours) average_hours,

            SUM(quizzes_completed) quizzes,

            SUM(flashcards_completed) flashcards,

            SUM(notes_created) notes,

            SUM(coding_sessions) coding,

            SUM(rag_queries) rag_queries,

            AVG(score) average_score

        FROM mentor_progress
        """

        return DBManager.fetch_one(sql)

    @staticmethod
    def weekly_progress():

        sql = """
        SELECT

            study_date,

            study_hours,

            score

        FROM mentor_progress

        WHERE study_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)

        ORDER BY study_date
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def monthly_progress():

        sql = """
        SELECT

            DATE_FORMAT(study_date,'%Y-%m') month,

            SUM(study_hours) hours,

            AVG(score) average_score

        FROM mentor_progress

        GROUP BY month

        ORDER BY month
        """

        return DBManager.fetch_all(sql)