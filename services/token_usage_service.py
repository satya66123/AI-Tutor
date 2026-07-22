"""
Token Usage Service
"""


class TokenUsageService:

    @staticmethod
    def estimate(text):

        words = len(text.split())

        tokens = int(words * 1.3)

        return {

            "words": words,

            "tokens": tokens

        }