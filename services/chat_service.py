"""
Chat Service
"""

from providers.provider_factory import ProviderFactory


class ChatService:
    """
    Handles AI chat requests.
    """

    @staticmethod
    def generate_response(prompt, model):

        provider = ProviderFactory.get_provider()

        return provider.generate_response(
            prompt=prompt,
            model=model
        )