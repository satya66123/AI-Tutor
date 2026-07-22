"""
Multi Query Service
"""

from services.chat_service import ChatService


class MultiQueryService:

    @staticmethod
    def generate(query):

        prompt = f"""
Generate 5 different search queries for the following question.

Rules:
- Preserve meaning.
- Use different wording.
- One query per line.

Question:
{query}
"""

        response = ChatService.generate_response(prompt)

        queries = [

            q.strip()

            for q in response.splitlines()

            if q.strip()

        ]

        return queries