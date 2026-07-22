"""
HyDE Service
"""

from services.chat_service import ChatService


class HyDEService:

    @staticmethod
    def generate(query):

        prompt = f"""
Write a hypothetical ideal answer to the following question.

The answer should be factual and informative.
It will only be used for semantic retrieval.

Question:

{query}
"""

        answer = ChatService.generate_response(prompt)

        return answer.strip()