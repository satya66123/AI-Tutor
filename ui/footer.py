"""
Footer Component
"""

import streamlit as st

from config.config import Config


class Footer:

    @staticmethod
    def render():

        st.divider()

        st.caption(
            f"{Config.APP_NAME} | Version {Config.APP_VERSION}"
        )