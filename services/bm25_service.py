"""
BM25 Search Service
"""

from rank_bm25 import BM25Okapi


class BM25Service:

    def __init__(self):

        self.documents = []
        self.tokenized_documents = []
        self.bm25 = None

    def build(self, documents):

        self.documents = documents

        self.tokenized_documents = [

            doc.lower().split()

            for doc in documents

        ]

        self.bm25 = BM25Okapi(

            self.tokenized_documents

        )

    def search(

        self,

        query,

        top_k=5

    ):

        if self.bm25 is None:

            return []

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(

            tokenized_query

        )

        ranked = sorted(

            enumerate(scores),

            key=lambda x: x[1],

            reverse=True

        )

        results = []

        for index, score in ranked[:top_k]:

            results.append({

                "index": index,

                "score": float(score),

                "text": self.documents[index]

            })

        return results