"""
Flashcards Parser
"""


class FlashcardParser:

    @staticmethod
    def extract(text):

        cards = []

        lines = text.splitlines()

        front = ""
        back = ""

        reading_front = False
        reading_back = False

        for line in lines:

            line = line.strip()

            if line.startswith("Flashcard"):

                if front and back:

                    cards.append({
                        "front": front.strip(),
                        "back": back.strip()
                    })

                front = ""
                back = ""

                reading_front = False
                reading_back = False

            elif line.startswith("Front:"):

                reading_front = True
                reading_back = False

                front = line.replace(
                    "Front:",
                    ""
                ).strip()

            elif line.startswith("Back:"):

                reading_front = False
                reading_back = True

                back = line.replace(
                    "Back:",
                    ""
                ).strip()

            else:

                if reading_front:

                    front += " " + line

                elif reading_back:

                    back += " " + line

        if front and back:

            cards.append({
                "front": front.strip(),
                "back": back.strip()
            })

        return cards