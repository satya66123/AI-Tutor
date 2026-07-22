"""
Coding Tutor Prompt Builder
"""


class CodingPromptBuilder:

    @staticmethod
    def build(
        task,
        language,
        code
    ):

        return f"""
You are an expert software engineer.

Programming Language:
{language}

Task:
{task}

Code:

{code}

Provide a detailed, well-formatted response using Markdown.

If generating code, return complete executable code.
"""