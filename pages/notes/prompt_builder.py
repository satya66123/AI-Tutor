"""
Notes Prompt Builder
"""


class NotesPromptBuilder:

    @staticmethod
    def build(
        topic,
        note_type,
        difficulty,
        words
    ):

        return f"""
Generate {note_type} on:

Topic:
{topic}

Difficulty:
{difficulty}

Length:
Approximately {words} words.

Requirements:

- Use headings.
- Use bullet points wherever appropriate.
- Keep the content clear and well organized.
- Explain concepts simply.
- Do not include introductions like
"Here are your notes."
Only output the notes.
"""