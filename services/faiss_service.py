"""
Enterprise FAISS Service
"""

import os
import pickle

import faiss
import numpy as np

from config.config import Config


class FAISSService:

    def __init__(self):

        self.dimension = 768

        self.index = None

        self.metadata = []

        self.load()

    def create(self, dimension):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

    def add(self, embeddings, metadata):

        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        if self.index is None:

            self.create(vectors.shape[1])

        self.index.add(vectors)

        self.metadata.extend(metadata)

    def search(self, embedding, top_k=5):

        vector = np.array(
            [embedding],
            dtype="float32"
        )

        distances, indexes = self.index.search(

            vector,

            top_k

        )

        results = []

        for distance, index in zip(

            distances[0],

            indexes[0]

        ):

            if index >= len(self.metadata):

                continue

            item = self.metadata[index].copy()

            item["score"] = float(distance)

            results.append(item)

        return results

    def save(self):

        os.makedirs(

            os.path.dirname(Config.FAISS_INDEX_PATH),

            exist_ok=True

        )

        faiss.write_index(

            self.index,

            Config.FAISS_INDEX_PATH

        )

        with open(

            Config.FAISS_METADATA_PATH,

            "wb"

        ) as file:

            pickle.dump(

                self.metadata,

                file

            )

    def load(self):

        if os.path.exists(

            Config.FAISS_INDEX_PATH

        ):

            self.index = faiss.read_index(

                Config.FAISS_INDEX_PATH

            )

        if os.path.exists(

            Config.FAISS_METADATA_PATH

        ):

            with open(

                Config.FAISS_METADATA_PATH,

                "rb"

            ) as file:

                self.metadata = pickle.load(file)

    def rebuild(self):

        self.index = None

        self.metadata = []

    def total_documents(self):

        return len(self.metadata)