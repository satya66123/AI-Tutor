"""
Interview Question Service
"""

import random

from database.db_manager import DBManager
from models.interview_models import InterviewQuestion


class InterviewQuestionService:

    @staticmethod
    def create(question: InterviewQuestion):

        sql = """
        INSERT INTO interview_questions
        (
            category,
            difficulty,
            question,
            answer,
            tags
        )
        VALUES
        (
            %s,%s,%s,%s,%s
        )
        """

        return DBManager.execute(

            sql,

            (

                question.category,

                question.difficulty,

                question.question,

                question.answer,

                question.tags

            )

        )

    @staticmethod
    def get_all():

        sql = """
        SELECT *

        FROM interview_questions

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def get(question_id):

        sql = """
        SELECT *

        FROM interview_questions

        WHERE id=%s
        """

        return DBManager.fetch_one(

            sql,

            (

                question_id,

            )

        )

    @staticmethod
    def update(question: InterviewQuestion):

        sql = """
        UPDATE interview_questions

        SET

            category=%s,

            difficulty=%s,

            question=%s,

            answer=%s,

            tags=%s

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                question.category,

                question.difficulty,

                question.question,

                question.answer,

                question.tags,

                question.id

            )

        )

    @staticmethod
    def delete(question_id):

        sql = """
        DELETE

        FROM interview_questions

        WHERE id=%s
        """

        return DBManager.execute(

            sql,

            (

                question_id,

            )

        )

    @staticmethod
    def by_category(category):

        sql = """
        SELECT *

        FROM interview_questions

        WHERE category=%s

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(

            sql,

            (

                category,

            )

        )

    @staticmethod
    def by_difficulty(difficulty):

        sql = """
        SELECT *

        FROM interview_questions

        WHERE difficulty=%s

        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(

            sql,

            (

                difficulty,

            )

        )

    @staticmethod
    def random_questions(

            category,

            difficulty,

            limit=10

    ):

        sql = """
        SELECT *

        FROM interview_questions

        WHERE

            category=%s

        AND

            difficulty=%s
        """

        questions = DBManager.fetch_all(

            sql,

            (

                category,

                difficulty

            )

        )

        if len(questions) <= limit:

            return questions

        return random.sample(

            questions,

            limit

        )

    @staticmethod
    def search(keyword):

        sql = """
        SELECT *

        FROM interview_questions

        WHERE

            question LIKE %s

        OR

            tags LIKE %s

        ORDER BY created_at DESC
        """

        search = f"%{keyword}%"

        return DBManager.fetch_all(

            sql,

            (

                search,

                search

            )

        )

    @staticmethod
    def statistics():

        sql = """
        SELECT

            COUNT(*) total_questions,

            COUNT(DISTINCT category) categories,

            COUNT(DISTINCT difficulty) difficulties

        FROM interview_questions
        """

        return DBManager.fetch_one(sql)
        