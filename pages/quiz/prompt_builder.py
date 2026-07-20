"""
Quiz Prompt Builder
"""


class QuizPromptBuilder:

    @staticmethod
    def build(topic, difficulty, quiz_type, questions):

        return f"""
Create exactly {questions} {quiz_type} questions on "{topic}".

Difficulty: {difficulty}

For every question provide four options A, B, C and D.

After all questions print exactly:

Answer Key

1. B
2. D
3. A
4. C
5. B

Do not explain anything.
Never omit the Answer Key.
"""