from automation.base_task import BaseTask


class QuizTask(BaseTask):

    def run(self, context):

        notes = context.get("notes")

        quiz = f"Quiz generated from {notes}"

        context.set("quiz", quiz)

        return {
            "quiz": quiz
        }