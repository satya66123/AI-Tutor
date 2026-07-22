"""
Citation Service
"""


class CitationService:

    @staticmethod
    def build(sources):

        citations = []

        for index, source in enumerate(sources, start=1):

            citations.append({

                "id": index,

                "document": source.get(

                    "document",

                    "Unknown"

                ),

                "chunk": source.get(

                    "chunk_id",

                    "-"

                )

            })

        return citations