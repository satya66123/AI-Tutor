"""
Interview History Service
"""

from database.db_manager import DBManager


class InterviewHistoryService:

    @staticmethod
    def save(

            session_id,

            interview_type,

            total_questions,

            score,

            duration,

            provider,

            model

    ):

        sql = """
        INSERT INTO interview_history
        (

            session_id,

            interview_type,

            total_questions,

            score,

            duration,

            provider,

            model

        )

        VALUES

        (

            %s,

            %s,

            %s,

            %s,

            %s,

            %s,

            %s

        )
        """

        return DBManager.execute(

            sql,

            (

                session_id,

                interview_type,

                total_questions,

                score,

                duration,

                provider,

                model

            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *

        FROM interview_history

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def get(session_id):

        sql = """
        SELECT *

        FROM interview_history

        WHERE session_id=%s
        """

        return DBManager.fetch_one(

            sql,

            (

                session_id,

            )

        )

    @staticmethod
    def delete(history_id):

        sql = """
        DELETE

        FROM interview_history

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                history_id,

            )

        )

    @staticmethod
    def clear():

        sql = """
        DELETE FROM interview_history
        """

        return DBManager.execute(sql)

    @staticmethod
    def by_type(interview_type):

        sql = """
        SELECT *

        FROM interview_history

        WHERE interview_type=%s

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(

            sql,

            (

                interview_type,

            )

        )

    @staticmethod
    def top_scores(limit=10):

        sql = """
        SELECT *

        FROM interview_history

        ORDER BY score DESC

        LIMIT %s
        """

        return DBManager.fetch_all(

            sql,

            (

                limit,

            )

        )

    @staticmethod
    def recent(limit=10):

        sql = """
        SELECT *

        FROM interview_history

        ORDER BY created_at DESC

        LIMIT %s
        """

        return DBManager.fetch_all(

            sql,

            (

                limit,

            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_interviews,

            AVG(score) average_score,

            MAX(score) highest_score,

            MIN(score) lowest_score,

            AVG(duration) average_duration,

            SUM(total_questions) total_questions

        FROM interview_history
        """

        return DBManager.fetch_one(sql)

    @staticmethod
    def score_distribution():

        sql = """
        SELECT

            CASE

                WHEN score>=9 THEN 'Excellent'

                WHEN score>=8 THEN 'Very Good'

                WHEN score>=7 THEN 'Good'

                WHEN score>=6 THEN 'Average'

                ELSE 'Needs Improvement'

            END performance,

            COUNT(*) total

        FROM interview_history

        GROUP BY performance
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def provider_statistics():

        sql = """
        SELECT

            provider,

            COUNT(*) interviews,

            AVG(score) average_score

        FROM interview_history

        GROUP BY provider
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def model_statistics():

        sql = """
        SELECT

            model,

            COUNT(*) interviews,

            AVG(score) average_score

        FROM interview_history

        GROUP BY model
        """

        return DBManager.fetch_all(sql)