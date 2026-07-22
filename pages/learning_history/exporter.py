"""
History Exporter
"""

import json
import streamlit as st


class HistoryExporter:

    @staticmethod
    def download(history):

        st.download_button(

            "📥 Export History",

            json.dumps(

                history,

                indent=4,

                default=str

            ),

            "learning_history.json",

            "application/json"

        )