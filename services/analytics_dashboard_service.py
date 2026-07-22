"""
Enterprise Analytics Dashboard
"""

from services.mysql_service import MySQLService


class AnalyticsDashboardService:

    @staticmethod
    def statistics():

        docs = MySQLService.fetch_one(

            "SELECT COUNT(*) total FROM documents"

        )

        chunks = MySQLService.fetch_one(

            "SELECT COUNT(*) total FROM document_chunks"

        )

        searches = MySQLService.fetch_one(

            "SELECT COUNT(*) total FROM retrieval_history"

        )

        return {

            "documents": docs["total"],

            "chunks": chunks["total"],

            "searches": searches["total"]

        }