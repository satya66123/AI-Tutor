class RAGPromptBuilder:

    @staticmethod
    def build(

        query,

        context,

        memory=""

    ):

        return f"""
You are an AI Tutor.

Conversation History

{memory}

Retrieved Context

{context}

Question

{query}

Instructions

- Answer ONLY from retrieved context.
- If information is unavailable, clearly say so.
- Explain step-by-step.
- Use markdown formatting.
"""