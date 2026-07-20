"""
Settings UI
"""

import streamlit as st

from pages.settings.settings_manager import SettingsManager
from pages.settings.defaults import DEFAULT_SETTINGS
from utils.notifications import Notifications


class SettingsUI:

    @staticmethod
    def render():

        SettingsManager.initialize()

        settings = SettingsManager.get()

        st.subheader("⚙ AI Configuration")

        st.markdown("### Model Parameters")

        temperature = st.slider(
            "Temperature",
            0.0,
            2.0,
            float(settings["temperature"]),
            0.1
        )

        max_tokens = st.number_input(
            "Max Tokens",
            128,
            8192,
            int(settings["max_tokens"])
        )

        top_p = st.slider(
            "Top P",
            0.0,
            1.0,
            float(settings["top_p"]),
            0.05
        )

        st.divider()

        st.markdown("### Tutor Preferences")

        response_length = st.selectbox(
            "Response Length",
            [
                "Short",
                "Medium",
                "Detailed"
            ],
            index=[
                "Short",
                "Medium",
                "Detailed"
            ].index(settings["response_length"])
        )

        learning_style = st.selectbox(
            "Learning Style",
            [
                "Balanced",
                "Visual",
                "Practical",
                "Theory First"
            ],
            index=[
                "Balanced",
                "Visual",
                "Practical",
                "Theory First"
            ].index(settings["learning_style"])
        )

        language = st.selectbox(
            "Language",
            [
                "English",
                "Telugu",
                "Hindi"
            ],
            index=[
                "English",
                "Telugu",
                "Hindi"
            ].index(settings["language"])
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("💾 Save Settings"):

                SettingsManager.update(
                    "temperature",
                    temperature
                )

                SettingsManager.update(
                    "max_tokens",
                    max_tokens
                )

                SettingsManager.update(
                    "top_p",
                    top_p
                )

                SettingsManager.update(
                    "response_length",
                    response_length
                )

                SettingsManager.update(
                    "learning_style",
                    learning_style
                )

                SettingsManager.update(
                    "language",
                    language
                )


                Notifications.success(
                    "Settings Saved Successfully"
                )

        with col2:

            if st.button("🔄 Reset"):

                SettingsManager.reset()

                st.rerun()

        with st.expander("Current Settings"):

            st.json(SettingsManager.get())