"""
Anthropic Provider
"""

import anthropic

from config.config import Config
from providers.base_provider import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):

        self.client = anthropic.Anthropic(
            api_key=Config.ANTHROPIC_API_KEY
        )

    def is_available(self):

        return bool(Config.ANTHROPIC_API_KEY)

    def list_models(self):

        """
        Anthropic currently doesn't provide
        a public List Models API.
        """

        return [
            "claude-opus-4-1",
            "claude-sonnet-4",
            "claude-3-7-sonnet-latest",
            "claude-3-5-haiku-latest"
        ]

    def generate_response(self, prompt, model):

        try:

            response = self.client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.content[0].text

        except Exception as e:

            return f"Error: {e}"