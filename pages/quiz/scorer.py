"""
Quiz Scorer
"""


class QuizScorer:

    @staticmethod
    def calculate(correct, total):

        if total == 0:

            return {
                "correct": 0,
                "wrong": 0,
                "total": 0,
                "percentage": 0,
                "status": "NO ANSWER KEY"
            }

        wrong = total - correct

        percentage = round((correct * 100) / total, 2)

        status = "PASS" if percentage >= 40 else "FAIL"

        return {

            "correct": correct,
            "wrong": wrong,
            "total": total,
            "percentage": percentage,
            "status": status

        }