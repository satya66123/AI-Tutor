"""
Chat Exporter
"""

import json
import streamlit as st


class ChatExporter:

    @staticmethod
    def export(messages):

        text = json.dumps(
            messages,
            indent=4
        )

        st.download_button(
            label="⬇ Download Chat",
            data=text,
            file_name="chat_history.json",
            mime="application/json"
        )