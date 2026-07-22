"""
Enterprise Health Check Service
"""

from services.faiss_service import FAISSService


class HealthCheckService:

    @staticmethod
    def check():

        faiss = FAISSService()

        return {

            "faiss_loaded": faiss.index is not None,

            "dimension": getattr(

                faiss,

                "dimension",

                "Unknown"

            )

        }