"""
Reranker Service
"""


class RerankerService:

    @staticmethod
    def rerank(results):

        if not results:

            return results

        return sorted(

            results,

            key=lambda item: item.get(

                "score",

                0

            )

        )