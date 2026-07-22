"""
Notes Service
"""

from pages.notes.prompt_builder import NotesPromptBuilder

from services.chat_service import ChatService


class NotesService:

    @staticmethod
    def generate(
        topic,
        note_type,
        difficulty,
        words,
        model
    ):

        prompt = NotesPromptBuilder.build(

            topic,

            note_type,

            difficulty,

            words

        )

        return ChatService.generate_response(

            prompt=prompt,

            model=model

        )