"""
Streaming Service
"""

import time


class StreamingService:

    @staticmethod
    def stream(text, placeholder, delay=0.01):

        current = ""

        for word in text.split():

            current += word + " "

            placeholder.markdown(current)

            time.sleep(delay)

        return current