"""
AI Mentor Service
"""

from services.goal_service import GoalService
from services.progress_service import ProgressService
from services.recommendation_service import RecommendationService
from services.weakness_service import WeaknessService
from services.insight_service import InsightService

from services.chat_service import ChatService
from services.memory_service import MemoryService
from services.session_service import SessionService
from services.response_time_service import ResponseTimeService
from services.token_usage_service import TokenUsageService

from database.db_manager import DBManager


class AIMentorService:

    @staticmethod
    def dashboard():

        return {

            "goals": GoalService.statistics(),

            "progress": ProgressService.statistics(),

            "recommendations": RecommendationService.statistics(),

            "weakness": WeaknessService.summary(),

            "insights": InsightService.latest()

        }

    @staticmethod
    def recommendations():

        RecommendationService.save_generated()

        return RecommendationService.get_pending()

    @staticmethod
    def weaknesses():

        return WeaknessService.summary()

    @staticmethod
    def insights():

        InsightService.save()

        return InsightService.latest()

    @staticmethod
    def mentor_chat(

            question,

            model,

            provider="Ollama"

    ):

        dashboard = AIMentorService.dashboard()

        memory = MemoryService.get_context()

        prompt = f"""
You are an AI Learning Mentor.

Answer the student's question.

Current Dashboard

Goals
{dashboard['goals']}

Progress
{dashboard['progress']}

Weaknesses
{dashboard['weakness']}

Recommendations
{dashboard['recommendations']}

Conversation Memory

{memory}

Student Question

{question}

Provide

• Personalized advice

• Improvement suggestions

• Motivation

• Actionable next steps
"""

        start = ResponseTimeService.start()

        answer = ChatService.generate_response(

            prompt=prompt,

            model=model

        )

        response_time = ResponseTimeService.stop(start)

        usage = TokenUsageService.estimate(answer)

        MemoryService.add(

            question,

            answer

        )

        session_id = SessionService.create()

        DBManager.execute(

            """
            INSERT INTO mentor_sessions
            (

                session_id,

                question,

                answer,

                provider,

                model,

                response_time,

                token_usage

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
            """,

            (

                session_id,

                question,

                answer,

                provider,

                model,

                response_time,

                usage

            )

        )

        return {

            "session_id": session_id,

            "answer": answer,

            "response_time": response_time,

            "token_usage": usage

        }

    @staticmethod
    def session_history():

        sql = """
        SELECT *

        FROM mentor_sessions

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def clear_sessions():

        sql = """
        DELETE FROM mentor_sessions
        """

        return DBManager.execute(sql)

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_sessions,

            AVG(response_time) average_response_time,

            AVG(token_usage) average_tokens

        FROM mentor_sessions
        """

        return DBManager.fetch_one(sql)