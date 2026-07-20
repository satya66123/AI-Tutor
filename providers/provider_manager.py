"""
Provider Manager
"""

from config.config import Config


class ProviderManager:
    """
    Manages the active AI provider.
    """

    _provider = Config.DEFAULT_PROVIDER

    @classmethod
    def get_provider(cls):
        return cls._provider

    @classmethod
    def set_provider(cls, provider):
        cls._provider = provider