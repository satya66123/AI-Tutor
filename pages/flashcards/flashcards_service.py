"""
Flashcards Service
"""

from pages.flashcards.prompt_builder import FlashcardPromptBuilder

from services.chat_service import ChatService


class FlashcardsService:

    @staticmethod
    def generate(
        topic,
        difficulty,
        cards,
        model
    ):

        prompt = FlashcardPromptBuilder.build(
            topic,
            difficulty,
            cards
        )

        return ChatService.generate_response(
            prompt=prompt,
            model=model
        )