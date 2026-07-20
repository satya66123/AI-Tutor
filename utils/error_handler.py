"""
Error Handler
"""

import streamlit as st

from loguru import logger


class ErrorHandler:

    @staticmethod
    def handle(error):

        logger.exception(error)

        st.error(
            f"Unexpected Error:\n\n{error}"
        )