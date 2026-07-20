"""
Quiz Evaluator
"""

from pages.quiz.scorer import QuizScorer


class QuizEvaluator:

    @staticmethod
    def evaluate(user_answers, answer_key):

        correct = 0

        for number, answer in answer_key.items():

            user = user_answers.get(number, "").strip().lower()

            if user == answer.lower():

                correct += 1

        return QuizScorer.calculate(
            correct,
            len(answer_key)
        )