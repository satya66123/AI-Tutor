"""
Notification Manager
"""

import streamlit as st


class Notifications:

    @staticmethod
    def success(message):

        st.success(message)

    @staticmethod
    def error(message):

        st.error(message)

    @staticmethod
    def warning(message):

        st.warning(message)

    @staticmethod
    def info(message):

        st.info(message)