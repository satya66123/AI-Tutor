"""
Enterprise Voice Session Service
"""

import uuid

from services.mysql_service import MySQLService


class VoiceSessionService:

    TABLE = "voice_sessions"

    # =====================================================
    # Create Session
    # =====================================================

    @staticmethod
    def create_session(

            provider,

            model,

            language="en"

    ):

        session_id = str(uuid.uuid4())

        sql = f"""
        INSERT INTO {VoiceSessionService.TABLE}
        (
            session_id,
            provider,
            model,
            language,
            status
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """

        MySQLService.execute(

            sql,

            (

                session_id,

                provider,

                model,

                language,

                "ACTIVE"

            )

        )

        return session_id

    # =====================================================
    # Get Session
    # =====================================================

    @staticmethod
    def get_session(session_id):

        sql = f"""
        SELECT *
        FROM {VoiceSessionService.TABLE}
        WHERE session_id=%s
        """

        return MySQLService.fetch_one(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Get All Sessions
    # =====================================================

    @staticmethod
    def get_sessions():

        sql = f"""
        SELECT *
        FROM {VoiceSessionService.TABLE}
        ORDER BY started_at DESC
        """

        return MySQLService.fetch_all(sql)

    # =====================================================
    # Update Status
    # =====================================================

    @staticmethod
    def update_status(

            session_id,

            status

    ):

        sql = f"""
        UPDATE {VoiceSessionService.TABLE}
        SET
            status=%s
        WHERE
            session_id=%s
        """

        MySQLService.execute(

            sql,

            (

                status,

                session_id

            )

        )

    # =====================================================
    # Increment Messages
    # =====================================================

    @staticmethod
    def increment_messages(session_id):

        sql = f"""
        UPDATE {VoiceSessionService.TABLE}
        SET
            total_messages = total_messages + 1
        WHERE
            session_id=%s
        """

        MySQLService.execute(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Update Duration
    # =====================================================

    @staticmethod
    def update_duration(

            session_id,

            duration

    ):

        sql = f"""
        UPDATE {VoiceSessionService.TABLE}
        SET
            total_duration=%s
        WHERE
            session_id=%s
        """

        MySQLService.execute(

            sql,

            (

                duration,

                session_id

            )

        )

    # =====================================================
    # Complete Session
    # =====================================================

    @staticmethod
    def complete_session(session_id):

        sql = f"""
        UPDATE {VoiceSessionService.TABLE}
        SET

            status='COMPLETED',

            ended_at=NOW()

        WHERE

            session_id=%s
        """

        MySQLService.execute(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Delete Session
    # =====================================================

    @staticmethod
    def delete_session(session_id):

        sql = f"""
        DELETE
        FROM {VoiceSessionService.TABLE}
        WHERE
            session_id=%s
        """

        MySQLService.execute(

            sql,

            (

                session_id,

            )

        )

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def get_statistics():

        sql = f"""
        SELECT

            COUNT(*) AS total_sessions,

            SUM(total_messages) AS total_messages,

            AVG(total_duration) AS average_duration,

            MAX(total_duration) AS longest_session

        FROM

            {VoiceSessionService.TABLE}
        """

        return MySQLService.fetch_one(sql)