"""
Provider Service
"""

from providers.provider_factory import ProviderFactory


class ProviderService:
    """
    Service for managing providers.
    """

    @staticmethod
    def get_provider():
        return ProviderFactory.get_provider()

    @staticmethod
    def is_provider_available():
        provider = ProviderFactory.get_provider()
        return provider.is_available()