"""
Interview Evaluation Service
"""

from database.db_manager import DBManager


class InterviewEvaluationService:

    @staticmethod
    def get_answers(session_id):

        sql = """
        SELECT *

        FROM interview_answers

        WHERE session_id=%s

        ORDER BY id
        """

        return DBManager.fetch_all(

            sql,

            (

                session_id,

            )

        )

    @staticmethod
    def overall_score(session_id):

        sql = """
        SELECT

            AVG(score) average_score,

            MAX(score) highest_score,

            MIN(score) lowest_score,

            COUNT(*) total_questions

        FROM interview_answers

        WHERE session_id=%s
        """

        result = DBManager.fetch_one(

            sql,

            (

                session_id,

            )

        )

        if result is None:

            return {

                "average_score":0,

                "highest_score":0,

                "lowest_score":0,

                "total_questions":0

            }

        return result

    @staticmethod
    def strengths(session_id):

        sql = """
        SELECT

            question,

            score

        FROM interview_answers

        WHERE

            session_id=%s

        AND

            score>=8

        ORDER BY score DESC
        """

        return DBManager.fetch_all(

            sql,

            (

                session_id,

            )

        )

    @staticmethod
    def weaknesses(session_id):

        sql = """
        SELECT

            question,

            score

        FROM interview_answers

        WHERE

            session_id=%s

        AND

            score<6

        ORDER BY score
        """

        return DBManager.fetch_all(

            sql,

            (

                session_id,

            )

        )

    @staticmethod
    def performance_level(score):

        if score >= 9:

            return "Excellent"

        elif score >= 8:

            return "Very Good"

        elif score >= 7:

            return "Good"

        elif score >= 6:

            return "Average"

        elif score >= 5:

            return "Needs Improvement"

        return "Poor"

    @staticmethod
    def summary(session_id):

        overall = InterviewEvaluationService.overall_score(

            session_id

        )

        strengths = InterviewEvaluationService.strengths(

            session_id

        )

        weaknesses = InterviewEvaluationService.weaknesses(

            session_id

        )

        score = overall["average_score"] or 0

        return {

            "overall_score": round(score,2),

            "performance":

                InterviewEvaluationService.performance_level(

                    score

                ),

            "total_questions":

                overall["total_questions"],

            "highest_score":

                overall["highest_score"],

            "lowest_score":

                overall["lowest_score"],

            "strengths":

                strengths,

            "weaknesses":

                weaknesses

        }

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_answers,

            AVG(score) average_score,

            MAX(score) highest_score,

            MIN(score) lowest_score

        FROM interview_answers
        """

        return DBManager.fetch_one(sql)