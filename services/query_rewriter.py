"""
Query Rewriter Service
"""

from services.chat_service import ChatService


class QueryRewriter:

    @staticmethod
    def rewrite(query):

        prompt = f"""
Rewrite the following search query to improve document retrieval.

Requirements:
- Keep the meaning unchanged.
- Make it more specific.
- Return only the rewritten query.

Query:
{query}
"""

        rewritten = ChatService.generate_response(prompt)

        return rewritten.strip()