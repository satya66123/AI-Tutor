"""
Provider Factory
"""

from providers.provider_manager import ProviderManager
from providers.ollama_provider import OllamaProvider
from providers.openai_provider import OpenAIProvider
from providers.anthropic_provider import AnthropicProvider


class ProviderFactory:
    """
    Returns the active provider instance.
    """

    @staticmethod
    def get_provider():

        provider = ProviderManager.get_provider()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "openai":
            return OpenAIProvider()

        if provider == "anthropic":
            return AnthropicProvider()

        raise ValueError(f"Unsupported provider: {provider}")