"""
PDF Tutor Service
"""

from services.chat_service import ChatService

from pages.pdf_tutor.prompt_builder import PDFPromptBuilder


class PDFTutorService:

    @staticmethod
    def ask(
        context,
        question,
        model
    ):

        prompt = PDFPromptBuilder.build(
            context,
            question
        )

        return ChatService.generate_response(

            prompt=prompt,

            model=model

        )