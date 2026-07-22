"""
Parent Child Retriever
"""

from collections import defaultdict


class ParentChildRetriever:

    @staticmethod
    def retrieve(results):

        grouped = defaultdict(list)

        for item in results:

            document = item.get("document", "Unknown")

            grouped[document].append(item)

        parents = []

        for document, chunks in grouped.items():

            parents.append({

                "document": document,

                "chunks": chunks,

                "text": "\n\n".join(

                    chunk["text"]

                    for chunk in chunks

                )

            })

        return parents