"""
Flashcards Prompt Builder
"""


class FlashcardPromptBuilder:

    @staticmethod
    def build(
        topic,
        difficulty,
        cards
    ):

        return f"""
Create exactly {cards} flashcards on "{topic}".

Difficulty: {difficulty}

Format exactly like this:

Flashcard 1
Front:
What is Python?

Back:
Python is a high-level programming language.

Flashcard 2
Front:
...

Back:
...

Do not add introductions.
Do not add explanations.
Only output flashcards.
"""