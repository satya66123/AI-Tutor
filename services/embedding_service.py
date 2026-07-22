"""
Enterprise Embedding Service
"""

import requests

from config.config import Config


class EmbeddingService:

    MODEL = Config.OLLAMA_EMBEDDING_MODEL

    @staticmethod
    def generate(text):

        response = requests.post(

            f"{Config.OLLAMA_HOST}/api/embeddings",

            json={

                "model": EmbeddingService.MODEL,

                "prompt": text

            },

            timeout=120

        )

        response.raise_for_status()

        return response.json()["embedding"]

    @staticmethod
    def generate_batch(chunks):

        embeddings = []

        for chunk in chunks:

            embeddings.append(

                EmbeddingService.generate(

                    chunk

                )

            )

        return embeddings