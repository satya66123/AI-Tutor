"""
Response Renderer
"""

import streamlit as st

from pages.tutor.stream_handler import StreamHandler


class ResponseRenderer:

    @staticmethod
    def render(role, message, stream=False):

        with st.chat_message(role):

            if stream:

                StreamHandler.stream_text(message)

            else:

                st.markdown(message)