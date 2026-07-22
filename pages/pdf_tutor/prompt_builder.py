"""
PDF Prompt Builder
"""


class PDFPromptBuilder:

    @staticmethod
    def build(
        context,
        question
    ):

        return f"""
You are an AI Tutor.

Answer ONLY using the PDF content below.

If the answer is not found in the PDF,
reply:

"I could not find that information in the uploaded document."

PDF Context

{context}

Question

{question}

Answer:
"""