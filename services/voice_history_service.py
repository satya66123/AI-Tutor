"""
Enterprise Voice History Service
"""

from services.mysql_service import MySQLService


class VoiceHistoryService:

    TABLE = "voice_history"

    # =====================================================
    # Save Conversation
    # =====================================================

    @staticmethod
    def save(

            session_id,

            transcript,

            ai_response,

            provider,

            model,

            language="en"

    ):

        sql = f"""
        INSERT INTO {VoiceHistoryService.TABLE}
        (

            session_id,

            transcript,

            ai_response,

            provider,

            model,

            language

        )
        VALUES
        (

            %s,

            %s,

            %s,

            %s,

            %s,

            %s

        )
        """

        return MySQLService.execute(

            sql,

            (

                session_id,

                transcript,

                ai_response,

                provider,

                model,

                language

            )

        )

    # =====================================================
    # Get Session History
    # =====================================================

    @staticmethod
    def get_session(session_id):

        sql = f"""
        SELECT *

        FROM {VoiceHistoryService.TABLE}

        WHERE session_id=%s

        ORDER BY created_at
        """

        return MySQLService.fetch_all(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Get All History
    # =====================================================

    @staticmethod
    def get_all(limit=100):

        sql = f"""
        SELECT *

        FROM {VoiceHistoryService.TABLE}

        ORDER BY created_at DESC

        LIMIT %s
        """

        return MySQLService.fetch_all(

            sql,

            (

                limit,

            )

        )

    # =====================================================
    # Search
    # =====================================================

    @staticmethod
    def search(keyword):

        value = f"%{keyword}%"

        sql = f"""
        SELECT *

        FROM {VoiceHistoryService.TABLE}

        WHERE

            transcript LIKE %s

            OR

            ai_response LIKE %s

        ORDER BY created_at DESC
        """

        return MySQLService.fetch_all(

            sql,

            (

                value,

                value

            )

        )

    # =====================================================
    # Delete Session
    # =====================================================

    @staticmethod
    def delete(session_id):

        sql = f"""
        DELETE

        FROM {VoiceHistoryService.TABLE}

        WHERE session_id=%s
        """

        return MySQLService.execute(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Clear History
    # =====================================================

    @staticmethod
    def clear():

        sql = f"""

        DELETE

        FROM {VoiceHistoryService.TABLE}

        """

        return MySQLService.execute(sql)

    # =====================================================
    # Total Conversations
    # =====================================================

    @staticmethod
    def total():

        sql = f"""

        SELECT

            COUNT(*) AS total

        FROM {VoiceHistoryService.TABLE}

        """

        row = MySQLService.fetch_one(sql)

        return row["total"]

    # =====================================================
    # Session Count
    # =====================================================

    @staticmethod
    def session_count():

        sql = f"""

        SELECT

            COUNT(DISTINCT session_id) AS total

        FROM {VoiceHistoryService.TABLE}

        """

        row = MySQLService.fetch_one(sql)

        return row["total"]

    # =====================================================
    # Recent Conversations
    # =====================================================

    @staticmethod
    def recent(limit=10):

        sql = f"""

        SELECT *

        FROM {VoiceHistoryService.TABLE}

        ORDER BY created_at DESC

        LIMIT %s

        """

        return MySQLService.fetch_all(

            sql,

            (

                limit,

            )

        )