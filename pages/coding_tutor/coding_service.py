"""
Coding Tutor Service
"""

from services.chat_service import ChatService

from pages.coding_tutor.prompt_builder import CodingPromptBuilder


class CodingTutorService:

    @staticmethod
    def process(
        task,
        language,
        code,
        model
    ):

        prompt = CodingPromptBuilder.build(
            task,
            language,
            code
        )

        return ChatService.generate_response(

            prompt=prompt,

            model=model

        )