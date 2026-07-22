"""
AI Mentor Weakness Service
"""

from database.db_manager import DBManager


class WeaknessService:

    @staticmethod
    def analyze():

        weaknesses = []

        # ---------------------------------
        # Quiz Performance
        # ---------------------------------

        quiz = DBManager.fetch_one("""

            SELECT

                AVG(score) average_score,

                COUNT(*) total_attempts

            FROM mentor_progress

        """)

        if quiz:

            score = quiz["average_score"] or 0

            if score < 60:

                weaknesses.append({

                    "category": "Quiz",

                    "severity": "High",

                    "title": "Low Quiz Performance",

                    "description":
                    "Average quiz score is below 60%."

                })

            elif score < 75:

                weaknesses.append({

                    "category": "Quiz",

                    "severity": "Medium",

                    "title": "Quiz Improvement Needed",

                    "description":
                    "Improve quiz consistency."

                })

        # ---------------------------------
        # Study Hours
        # ---------------------------------

        study = DBManager.fetch_one("""

            SELECT

                AVG(study_hours) hours

            FROM mentor_progress

        """)

        if study:

            hours = study["hours"] or 0

            if hours < 2:

                weaknesses.append({

                    "category": "Study",

                    "severity": "Medium",

                    "title": "Low Study Time",

                    "description":
                    "Average daily study time is below recommended."

                })

        # ---------------------------------
        # Coding Practice
        # ---------------------------------

        coding = DBManager.fetch_one("""

            SELECT

                SUM(coding_sessions) sessions

            FROM mentor_progress

        """)

        if coding:

            sessions = coding["sessions"] or 0

            if sessions < 5:

                weaknesses.append({

                    "category": "Coding",

                    "severity": "Medium",

                    "title": "Limited Coding Practice",

                    "description":
                    "Complete more coding exercises."

                })

        # ---------------------------------
        # Enterprise RAG Usage
        # ---------------------------------

        rag = DBManager.fetch_one("""

            SELECT

                SUM(rag_queries) total

            FROM mentor_progress

        """)

        if rag:

            queries = rag["total"] or 0

            if queries < 10:

                weaknesses.append({

                    "category": "Enterprise RAG",

                    "severity": "Low",

                    "title": "Low AI Tutor Usage",

                    "description":
                    "Use Enterprise RAG more frequently."

                })

        return weaknesses

    @staticmethod
    def summary():

        data = WeaknessService.analyze()

        return {

            "total": len(data),

            "high": len(

                [

                    x

                    for x in data

                    if x["severity"] == "High"

                ]

            ),

            "medium": len(

                [

                    x

                    for x in data

                    if x["severity"] == "Medium"

                ]

            ),

            "low": len(

                [

                    x

                    for x in data

                    if x["severity"] == "Low"

                ]

            ),

            "items": data

        }

    @staticmethod
    def top_priorities(limit=5):

        data = WeaknessService.analyze()

        priority = {

            "High": 1,

            "Medium": 2,

            "Low": 3

        }

        data.sort(

            key=lambda x: priority[x["severity"]]

        )

        return data[:limit]