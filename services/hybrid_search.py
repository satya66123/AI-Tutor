"""
Hybrid Search Service
"""


class HybridSearch:

    @staticmethod
    def reciprocal_rank_fusion(

        semantic_results,

        bm25_results,

        k=60

    ):

        scores = {}

        metadata = {}

        rank = 1

        for item in semantic_results:

            key = item["chunk_id"]

            scores[key] = scores.get(

                key,

                0

            ) + 1 / (k + rank)

            metadata[key] = item

            rank += 1

        rank = 1

        for item in bm25_results:

            key = item["index"]

            scores[key] = scores.get(

                key,

                0

            ) + 1 / (k + rank)

            metadata[key] = item

            rank += 1

        merged = sorted(

            scores.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return [

            metadata[item[0]]

            for item in merged

        ]