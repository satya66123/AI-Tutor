"""
AI Mentor Insight Service
"""

from database.db_manager import DBManager
from services.goal_service import GoalService
from services.progress_service import ProgressService
from services.recommendation_service import RecommendationService
from services.weakness_service import WeaknessService


class InsightService:

    @staticmethod
    def generate():

        insights = []

        # -----------------------------------
        # Goal Statistics
        # -----------------------------------

        goal_stats = GoalService.statistics()

        if goal_stats:

            completed = goal_stats["completed"] or 0

            total = goal_stats["total"] or 0

            if total > 0:

                percent = round((completed / total) * 100, 2)

                insights.append({

                    "type": "Goals",

                    "title": "Goal Completion",

                    "description":
                    f"You have completed {completed} of {total} goals ({percent}%)."

                })

        # -----------------------------------
        # Progress Statistics
        # -----------------------------------

        progress = ProgressService.statistics()

        if progress:

            hours = progress["total_hours"] or 0

            score = progress["average_score"] or 0

            insights.append({

                "type": "Progress",

                "title": "Learning Progress",

                "description":
                f"Total study hours: {hours:.2f}, Average score: {score:.2f}%."

            })

        # -----------------------------------
        # Weakness Summary
        # -----------------------------------

        weakness = WeaknessService.summary()

        insights.append({

            "type": "Weakness",

            "title": "Learning Gaps",

            "description":
            f"{weakness['high']} High, "
            f"{weakness['medium']} Medium, "
            f"{weakness['low']} Low priority weaknesses detected."

        })

        # -----------------------------------
        # Recommendation Summary
        # -----------------------------------

        recommendation = RecommendationService.statistics()

        if recommendation:

            insights.append({

                "type": "Recommendations",

                "title": "Pending Recommendations",

                "description":
                f"{recommendation['pending']} recommendation(s) waiting for action."

            })

        return insights

    @staticmethod
    def save():

        insights = InsightService.generate()

        for item in insights:

            DBManager.execute(

                """
                INSERT INTO mentor_insights
                (

                    insight_type,

                    title,

                    description,

                    generated_by

                )

                VALUES

                (

                    %s,

                    %s,

                    %s,

                    %s

                )
                """,

                (

                    item["type"],

                    item["title"],

                    item["description"],

                    "AI Mentor"

                )

            )

        return len(insights)

    @staticmethod
    def get_all():

        sql = """
        SELECT *

        FROM mentor_insights

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def latest(limit=10):

        sql = """
        SELECT *

        FROM mentor_insights

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
    def clear():

        sql = """
        DELETE FROM mentor_insights
        """

        return DBManager.execute(sql)