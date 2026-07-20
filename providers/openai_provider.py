"""
OpenAI Provider
"""

from openai import OpenAI

from config.config import Config
from providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

    def is_available(self):

        return bool(Config.OPENAI_API_KEY)

    def list_models(self):

        try:

            models = self.client.models.list()

            return sorted(
                [
                    model.id
                    for model in models.data
                    if "gpt" in model.id.lower()
                ]
            )

        except Exception as e:

            print(e)

            return []

    def generate_response(self, prompt, model):

        try:

            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

        except Exception as e:

            return f"Error: {e}"