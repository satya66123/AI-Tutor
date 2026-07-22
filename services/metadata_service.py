"""
Enterprise Metadata Service
"""


class MetadataService:

    @staticmethod
    def create(

        document,

        chunk_id,

        page,

        chapter,

        topic,

        text

    ):

        return {

            "document": document,

            "chunk_id": chunk_id,

            "page": page,

            "chapter": chapter,

            "topic": topic,

            "text": text

        }

    @staticmethod
    def filter(

        metadata,

        filters

    ):

        if not filters:

            return metadata

        results = []

        for item in metadata:

            matched = True

            for key, value in filters.items():

                if item.get(key) != value:

                    matched = False

                    break

            if matched:

                results.append(item)

        return results