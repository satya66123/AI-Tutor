from automation.base_task import BaseTask


class NotesTask(BaseTask):

    def run(self, context):

        document = context.get("document")

        notes = f"Generated Notes for {document}"

        context.set("notes", notes)

        return {
            "notes": notes
        }