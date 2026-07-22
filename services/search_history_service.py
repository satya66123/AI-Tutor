"""
Enterprise Search History Service
"""

from services.mysql_service import MySQLService


class SearchHistoryService:

    @staticmethod
    def get_history(limit=20):

        sql = """
        SELECT
            id,
            query,
            total_results,
            searched_at
        FROM retrieval_history
        ORDER BY searched_at DESC
        LIMIT %s
        """

        return MySQLService.fetch_all(

            sql,

            (limit,)

        )