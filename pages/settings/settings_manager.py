import streamlit as st

from pages.settings.defaults import DEFAULT_SETTINGS
from utils.json_manager import JsonManager


class SettingsManager:

    FILE_NAME = "settings.json"

    @staticmethod
    def initialize():

        if "settings" not in st.session_state:

            settings = JsonManager.load(
                SettingsManager.FILE_NAME,
                DEFAULT_SETTINGS
            )

            st.session_state.settings = settings

    @staticmethod
    def get():

        SettingsManager.initialize()

        return st.session_state.settings

    @staticmethod
    def update(key, value):

        SettingsManager.initialize()

        st.session_state.settings[key] = value

        JsonManager.save(
            SettingsManager.FILE_NAME,
            st.session_state.settings
        )

    @staticmethod
    def reset():

        st.session_state.settings = DEFAULT_SETTINGS.copy()

        JsonManager.save(
            SettingsManager.FILE_NAME,
            st.session_state.settings
        )