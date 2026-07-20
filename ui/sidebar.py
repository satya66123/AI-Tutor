"""
Sidebar Component
"""

import streamlit as st

from providers.provider_manager import ProviderManager
from services.model_service import ModelService


class Sidebar:

    @staticmethod
    def render():

        with st.sidebar:

            st.title("⚙ Settings")

            provider = st.selectbox(
                "Provider",
                [
                    "ollama",
                    "openai",
                    "anthropic"
                ],
                index=0
            )

            ProviderManager.set_provider(provider)

            models = ModelService.get_models()

            if models:

                default_model = ModelService.get_default_model()

                index = models.index(default_model)

                model = st.selectbox(
                    "Model",
                    models,
                    index=index
                )

            else:

                model = None

                st.warning("No Models Found")

            st.divider()

            st.success("Provider Ready")

            return provider, model