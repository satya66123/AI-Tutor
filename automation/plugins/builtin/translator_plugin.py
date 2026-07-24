from automation.plugins.plugin import Plugin


class TranslatorPlugin(Plugin):

    def __init__(self):

        super().__init__()

        self.name = "Translator Plugin"

        self.description = "Translate text"

        self.author = "Enterprise AI Tutor"

    def initialize(self):

        print("Translator initialized")

    def execute(
            self,
            context
    ):

        text = context.get("text")

        target = context.get(
            "target_language",
            "English"
        )

        return {

            "translated_text": text,

            "target_language": target

        }

    def shutdown(self):

        print("Translator stopped")