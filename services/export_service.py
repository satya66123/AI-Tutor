"""
Enterprise Export Service
"""

import json


class ExportService:

    @staticmethod
    def export_chat(chat_history):

        return json.dumps(

            chat_history,

            indent=4,

            default=str

        )