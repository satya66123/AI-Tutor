"""
Exception Service
"""

import traceback

from services.logging_service import LoggingService


class ExceptionService:

    @staticmethod
    def handle(exception):

        LoggingService.error(

            traceback.format_exc()

        )

        return {

            "success": False,

            "message": str(exception)

        }