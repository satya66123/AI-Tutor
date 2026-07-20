"""
Planner Service
"""

from services.chat_service import ChatService

from pages.planner.prompt_builder import PromptBuilder


class PlannerService:

    @staticmethod
    def generate(
        subject,
        level,
        goal,
        hours,
        duration,
        model
    ):

        prompt = PromptBuilder.build(
            subject,
            level,
            goal,
            hours,
            duration
        )

        return ChatService.generate_response(
            prompt,
            model
        )