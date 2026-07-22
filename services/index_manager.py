"""
Enterprise Index Manager
"""

from services.faiss_service import FAISSService


class IndexManager:

    @staticmethod
    def rebuild():

        faiss = FAISSService()

        faiss.rebuild()

        faiss.save()

    @staticmethod
    def clear():

        faiss = FAISSService()

        faiss.rebuild()

        faiss.save()

    @staticmethod
    def statistics():

        faiss = FAISSService()

        return {

            "indexed_chunks": faiss.total_documents(),

            "vector_dimension": getattr(
                faiss,
                "dimension",
                "Unknown"
            ),

            "index_loaded": faiss.index is not None

        }