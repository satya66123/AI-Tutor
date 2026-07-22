"""
Enterprise Cache Service
"""

from services.mysql_service import MySQLService


class CacheService:

    _hits = 0
    _misses = 0

    @classmethod
    def set(
            cls,
            question_hash,
            question,
            result,
            provider,
            model
    ):

        MySQLService.save_cache(

            question_hash,

            question,

            result,

            provider,

            model

        )

    @classmethod
    def get(cls, question_hash):

        result = MySQLService.get_cache(question_hash)

        if result:
            cls._hits += 1

            return result

        cls._misses += 1

        return None

    @classmethod
    def statistics(cls):

        total = cls._hits + cls._misses

        hit_rate = 0

        if total:
            hit_rate = round(

                (cls._hits / total) * 100,

                2

            )

        return {

            "entries": cls.size(),

            "hits": cls._hits,

            "misses": cls._misses,

            "hit_rate": hit_rate

        }

    @classmethod
    def clear(cls):
        """
        Clear the entire cache.
        """

        MySQLService.execute("DELETE FROM rag_cache")
        MySQLService.execute("ALTER TABLE rag_cache AUTO_INCREMENT = 1")

        cls._hits = 0
        cls._misses = 0

    @classmethod
    def size(cls):
        """
        Return total cache entries.
        """

        sql = """
        SELECT COUNT(*) AS total
        FROM rag_cache
        """

        result = MySQLService.fetch_one(sql)

        if result:
            return result["total"]

        return 0