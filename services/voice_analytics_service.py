"""
Voice Analytics Service
"""

from database.db_manager import DBManager
from models.voice_models import VoiceAnalytics


class VoiceAnalyticsService:

    TABLE = "voice_analytics"

    # --------------------------------------------------

    @staticmethod
    def save(analytics: VoiceAnalytics):

        query = f"""
        INSERT INTO {VoiceAnalyticsService.TABLE}
        (
            session_id,
            total_duration,
            speaking_duration,
            ai_duration,
            total_messages,
            average_response_time,
            provider,
            model
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        DBManager.execute(
            query,
            (
                analytics.session_id,
                analytics.total_duration,
                analytics.speaking_duration,
                analytics.ai_duration,
                analytics.total_messages,
                analytics.average_response_time,
                analytics.provider,
                analytics.model
            )
        )

    # --------------------------------------------------

    @staticmethod
    def update(session_id, analytics: VoiceAnalytics):

        query = f"""
        UPDATE {VoiceAnalyticsService.TABLE}
        SET
            total_duration=%s,
            speaking_duration=%s,
            ai_duration=%s,
            total_messages=%s,
            average_response_time=%s,
            provider=%s,
            model=%s
        WHERE
            session_id=%s
        """

        DBManager.execute(
            query,
            (
                analytics.total_duration,
                analytics.speaking_duration,
                analytics.ai_duration,
                analytics.total_messages,
                analytics.average_response_time,
                analytics.provider,
                analytics.model,
                session_id
            )
        )

    # --------------------------------------------------

    @staticmethod
    def get(session_id):

        query = f"""
        SELECT *
        FROM {VoiceAnalyticsService.TABLE}
        WHERE session_id=%s
        """

        return DBManager.fetch_one(
            query,
            (
                session_id,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def get_all():

        query = f"""
        SELECT *
        FROM {VoiceAnalyticsService.TABLE}
        ORDER BY created_at DESC
        """

        return DBManager.fetch_all(query)

    # --------------------------------------------------

    @staticmethod
    def delete(session_id):

        query = f"""
        DELETE
        FROM {VoiceAnalyticsService.TABLE}
        WHERE session_id=%s
        """

        DBManager.execute(
            query,
            (
                session_id,
            )
        )

    # --------------------------------------------------

    @staticmethod
    def clear():

        query = f"""
        DELETE
        FROM {VoiceAnalyticsService.TABLE}
        """

        DBManager.execute(query)

    # --------------------------------------------------

    @staticmethod
    def overall_statistics():

        query = f"""
        SELECT

            COUNT(*) AS total_sessions,

            SUM(total_messages) AS total_messages,

            AVG(total_duration) AS average_duration,

            AVG(average_response_time) AS average_response_time,

            MAX(total_duration) AS longest_session

        FROM {VoiceAnalyticsService.TABLE}
        """

        return DBManager.fetch_one(query)

    # --------------------------------------------------

    @staticmethod
    def provider_statistics():

        query = f"""
        SELECT

            provider,

            model,

            COUNT(*) AS sessions,

            AVG(total_duration) AS average_duration,

            SUM(total_messages) AS total_messages

        FROM {VoiceAnalyticsService.TABLE}

        GROUP BY provider, model

        ORDER BY sessions DESC
        """

        return DBManager.fetch_all(query)

    # --------------------------------------------------

    @staticmethod
    def top_sessions(limit=10):

        query = f"""
        SELECT *

        FROM {VoiceAnalyticsService.TABLE}

        ORDER BY total_duration DESC

        LIMIT %s
        """

        return DBManager.fetch_all(
            query,
            (
                limit,
            )
        )