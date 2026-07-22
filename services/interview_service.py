"""
Interview Service
"""

import uuid

from database.db_manager import DBManager

from services.chat_service import ChatService
from services.memory_service import MemoryService
from services.session_service import SessionService
from services.response_time_service import ResponseTimeService
from services.token_usage_service import TokenUsageService

from services.interview_question_service import InterviewQuestionService


class InterviewService:

    @staticmethod
    def start_session(

            interview_type,

            provider,

            model,

            difficulty,

            total_questions=10

    ):

        session_id = str(uuid.uuid4())

        questions = InterviewQuestionService.random_questions(

            interview_type,

            difficulty,

            total_questions

        )

        DBManager.execute(

            """
            INSERT INTO interview_sessions
            (

                session_id,

                interview_type,

                provider,

                model

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

                session_id,

                interview_type,

                provider,

                model

            )

        )

        return {

            "session_id": session_id,

            "questions": questions

        }

    @staticmethod
    def evaluate_answer(

            session_id,

            question,

            expected_answer,

            user_answer,

            provider,

            model

    ):

        memory = MemoryService.get_context()

        prompt = f"""
You are an AI Interviewer.

Interview Question

{question}

Expected Answer

{expected_answer}

Candidate Answer

{user_answer}

Conversation Memory

{memory}

Evaluate the answer and return:

1. Score (0-10)

2. Strengths

3. Weaknesses

4. Correct Answer

5. Suggestions
"""

        start = ResponseTimeService.start()

        feedback = ChatService.generate_response(

            prompt=prompt,

            model=model

        )

        response_time = ResponseTimeService.stop(start)

        tokens = TokenUsageService.estimate(feedback)

        MemoryService.add(

            question,

            user_answer

        )

        score = 0

        try:

            import re

            match = re.search(r'(\d+)', feedback)

            if match:

                score = float(match.group(1))

        except:

            pass

        DBManager.execute(

            """
            INSERT INTO interview_answers
            (

                session_id,

                question,

                user_answer,

                ai_feedback,

                score

            )

            VALUES

            (

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

                user_answer,

                feedback,

                score

            )

        )

        return {

            "score": score,

            "feedback": feedback,

            "response_time": response_time,

            "token_usage": tokens

        }

    @staticmethod
    def finish_session(session_id):

        DBManager.execute(

            """
            UPDATE interview_sessions

            SET

                completed_at=NOW()

            WHERE session_id=%s
            """,

            (

                session_id,

            )

        )

    @staticmethod
    def get_session(session_id):

        return DBManager.fetch_one(

            """
            SELECT *

            FROM interview_sessions

            WHERE session_id=%s
            """,

            (

                session_id,

            )

        )

    @staticmethod
    def session_answers(session_id):

        return DBManager.fetch_all(

            """
            SELECT *

            FROM interview_answers

            WHERE session_id=%s
            """,

            (

                session_id,

            )

        )

    @staticmethod
    def statistics():

        return DBManager.fetch_one(

            """
            SELECT

                COUNT(*) total_sessions,

                AVG(TIMESTAMPDIFF
                (

                    SECOND,

                    started_at,

                    completed_at

                )) average_duration

            FROM interview_sessions

            WHERE completed_at IS NOT NULL
            """

        )