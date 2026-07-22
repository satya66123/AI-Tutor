"""
Enterprise Chunk Service
"""

from pages.rag.models import ChunkStrategy


class ChunkService:

    @staticmethod
    def create_chunks(

        text,

        strategy,

        chunk_size,

        overlap

    ):

        if strategy == ChunkStrategy.FIXED.value:

            return ChunkService.fixed(

                text,

                chunk_size,

                overlap

            )

        if strategy == ChunkStrategy.RECURSIVE.value:

            return ChunkService.recursive(

                text,

                chunk_size,

                overlap

            )

        return ChunkService.fixed(

            text,

            chunk_size,

            overlap

        )

    @staticmethod
    def fixed(

        text,

        chunk_size,

        overlap

    ):

        chunks = []

        step = chunk_size - overlap

        start = 0

        while start < len(text):

            chunks.append(

                text[start:start+chunk_size]

            )

            start += step

        return chunks

    @staticmethod
    def recursive(

        text,

        chunk_size,

        overlap

    ):

        paragraphs = text.split("\n\n")

        chunks = []

        current = ""

        for paragraph in paragraphs:

            if len(current) + len(paragraph) < chunk_size:

                current += paragraph + "\n\n"

            else:

                chunks.append(current)

                current = paragraph

        if current:

            chunks.append(current)

        return chunks