"""
AI Mentor Recommendation Service
"""

from database.db_manager import DBManager


class RecommendationService:

    @staticmethod
    def create(

            recommendation_type,
            title,
            description,
            priority="Medium"

    ):

        sql = """
        INSERT INTO mentor_recommendations
        (
            recommendation_type,
            title,
            description,
            priority
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        """

        return DBManager.execute(

            sql,

            (

                recommendation_type,

                title,

                description,

                priority

            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *
        FROM mentor_recommendations
        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def get_pending():

        sql = """
        SELECT *
        FROM mentor_recommendations
        WHERE status='Pending'
        ORDER BY priority DESC, created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def update_status(

            recommendation_id,

            status

    ):

        sql = """
        UPDATE mentor_recommendations

        SET

            status=%s

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                status,

                recommendation_id

            )

        )

    @staticmethod
    def delete(recommendation_id):

        sql = """
        DELETE
        FROM mentor_recommendations
        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                recommendation_id,

            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total,

            SUM(status='Pending') pending,

            SUM(status='Accepted') accepted,

            SUM(status='Completed') completed

        FROM mentor_recommendations
        """

        return DBManager.fetch_one(sql)

    # --------------------------------------------------
    # AI Recommendation Engine
    # --------------------------------------------------

    @staticmethod
    def generate():

        recommendations = []

        # --------------------------
        # Progress Statistics
        # --------------------------

        progress = DBManager.fetch_one("""

            SELECT

                AVG(score) average_score,

                AVG(study_hours) average_hours,

                SUM(quizzes_completed) quizzes,

                SUM(coding_sessions) coding,

                SUM(rag_queries) rag

            FROM mentor_progress

        """)

        if progress:

            score = progress["average_score"] or 0

            hours = progress["average_hours"] or 0

            rag = progress["rag"] or 0

            coding = progress["coding"] or 0

            quizzes = progress["quizzes"] or 0

            if score < 60:

                recommendations.append(

                    {

                        "type": "Performance",

                        "title": "Improve Quiz Performance",

                        "description":
                        "Spend more time reviewing weak topics before attempting quizzes.",

                        "priority": "High"

                    }

                )

            if hours < 2:

                recommendations.append(

                    {

                        "type": "Study",

                        "title": "Increase Daily Study Time",

                        "description":
                        "Aim for at least two hours of focused learning each day.",

                        "priority": "Medium"

                    }

                )

            if rag < 5:

                recommendations.append(

                    {

                        "type": "Enterprise RAG",

                        "title": "Use AI Tutor More Frequently",

                        "description":
                        "Ask more questions using Enterprise RAG to reinforce concepts.",

                        "priority": "Medium"

                    }

                )

            if coding < 3:

                recommendations.append(

                    {

                        "type": "Coding",

                        "title": "Practice Coding",

                        "description":
                        "Complete additional coding exercises to improve problem-solving.",

                        "priority": "Medium"

                    }

                )

            if quizzes < 5:

                recommendations.append(

                    {

                        "type": "Quiz",

                        "title": "Attempt More Quizzes",

                        "description":
                        "Regular quizzes help reinforce long-term memory.",

                        "priority": "Low"

                    }

                )

        return recommendations

    @staticmethod
    def save_generated():

        recommendations = RecommendationService.generate()

        for item in recommendations:

            RecommendationService.create(

                item["type"],

                item["title"],

                item["description"],

                item["priority"]

            )

        return len(recommendations)