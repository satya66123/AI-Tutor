"""
Context Compression Service
"""


class ContextCompression:

    @staticmethod
    def compress(

        results,

        max_chunks=5

    ):

        if len(results) <= max_chunks:

            return results

        return results[:max_chunks]

    @staticmethod
    def compress_text(

        text,

        max_length=3000

    ):

        if len(text) <= max_length:

            return text

        return text[:max_length]