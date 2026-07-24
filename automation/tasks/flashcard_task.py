from automation.base_task import BaseTask


class FlashcardTask(BaseTask):

    def run(self, context):

        document = context.get("document")

        flashcards = f"Generated Flashcards for {document}"

        context.set("flashcards", flashcards)

        return {
            "flashcards": flashcards
        }