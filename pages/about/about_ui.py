"""
About UI
"""

import streamlit as st

from config.config import Config

from pages.about.features import FEATURES
from pages.about.technologies import TECHNOLOGIES


class AboutUI:

    @staticmethod
    def render():

        st.title("ℹ About AI Tutor")

        st.write(
            "AI Tutor is an intelligent learning assistant designed "
            "to help learners study, plan, and interact with multiple AI providers."
        )

        st.divider()

        st.subheader("✨ Features")

        for feature in FEATURES:

            st.write(feature)

        st.divider()

        st.subheader("🛠 Technologies")

        for category, values in TECHNOLOGIES.items():

            st.markdown(f"**{category}**")

            for value in values:

                st.write(f"- {value}")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Version",
                Config.APP_VERSION
            )

        with col2:

            st.metric(
                "Providers",
                "3"
            )

        st.divider()

        st.success("AI Tutor is ready for learning.")