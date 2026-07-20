"""
Base Provider Interface
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """

    @abstractmethod
    def generate_response(self, prompt: str, model: str):
        """Generate a response."""
        pass

    @abstractmethod
    def list_models(self):
        """Return available models."""
        pass

    @abstractmethod
    def is_available(self):
        """Check provider availability."""
        pass