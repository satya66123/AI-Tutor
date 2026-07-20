"""
Stream Handler
"""

import time
import streamlit as st


class StreamHandler:

    @staticmethod
    def stream_text(text: str):

        placeholder = st.empty()

        current = ""

        words = text.split()

        for word in words:

            current += word + " "

            placeholder.markdown(current)

            time.sleep(0.03)

        return text