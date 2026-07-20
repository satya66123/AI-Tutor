"""
Quiz Parser
"""

import re


class QuizParser:

    @staticmethod
    def extract_answers(text):

        answers = {}

        pattern = r"Answer Key(.*)"

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        if not match:
            return answers

        answer_text = match.group(1)

        lines = answer_text.splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            result = re.match(
                r"(\d+)[.):-]\s*(.+)",
                line
            )

            if result:

                number = int(result.group(1))

                answer = result.group(2).strip()

                answers[number] = answer

        return answers