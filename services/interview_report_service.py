"""
Interview Report Service
"""

from database.db_manager import DBManager
from services.interview_evaluation_service import InterviewEvaluationService


class InterviewReportService:

    @staticmethod
    def generate(session_id):

        evaluation = InterviewEvaluationService.summary(session_id)

        strengths = "\n".join(

            [

                f"- {item['question']} ({item['score']}/10)"

                for item in evaluation["strengths"]

            ]

        )

        weaknesses = "\n".join(

            [

                f"- {item['question']} ({item['score']}/10)"

                for item in evaluation["weaknesses"]

            ]

        )

        recommendations = []

        if evaluation["overall_score"] < 6:

            recommendations.append(
                "Revise the core concepts before the next interview."
            )

        elif evaluation["overall_score"] < 8:

            recommendations.append(
                "Practice more interview questions and mock interviews."
            )

        else:

            recommendations.append(
                "Maintain your preparation and focus on advanced topics."
            )

        return {

            "session_id": session_id,

            "overall_score": evaluation["overall_score"],

            "strengths": strengths,

            "weaknesses": weaknesses,

            "recommendations": "\n".join(recommendations)

        }

    @staticmethod
    def save(session_id):

        report = InterviewReportService.generate(session_id)

        sql = """
        INSERT INTO interview_reports
        (

            session_id,

            overall_score,

            strengths,

            weaknesses,

            recommendations

        )

        VALUES

        (

            %s,

            %s,

            %s,

            %s,

            %s

        )
        """

        DBManager.execute(

            sql,

            (

                report["session_id"],

                report["overall_score"],

                report["strengths"],

                report["weaknesses"],

                report["recommendations"]

            )

        )

        return report

    @staticmethod
    def get(session_id):

        sql = """
        SELECT *

        FROM interview_reports

        WHERE session_id=%s
        """

        return DBManager.fetch_one(

            sql,

            (

                session_id,

            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *

        FROM interview_reports

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def delete(report_id):

        sql = """
        DELETE

        FROM interview_reports

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                report_id,

            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_reports,

            AVG(overall_score) average_score,

            MAX(overall_score) highest_score,

            MIN(overall_score) lowest_score

        FROM interview_reports
        """

        return DBManager.fetch_one(sql)