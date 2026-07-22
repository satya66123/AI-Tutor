"""
Revision Planner Service
"""

from services.chat_service import ChatService

from pages.revision_planner.prompt_builder import PlannerPromptBuilder


class RevisionPlannerService:

    @staticmethod
    def generate(

        exam,

        subject,

        topics,

        exam_date,

        hours,

        difficulty,

        goal,

        plan_type,

        model

    ):

        prompt = PlannerPromptBuilder.build(

            exam,

            subject,

            topics,

            exam_date,

            hours,

            difficulty,

            goal,

            plan_type

        )

        return ChatService.generate_response(

            prompt=prompt,

            model=model

        )