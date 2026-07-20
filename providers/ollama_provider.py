"""
Ollama Provider
"""

import requests

from config.config import Config
from providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Ollama AI Provider
    """

    def __init__(self):
        self.base_url = Config.OLLAMA_HOST

    def is_available(self):
        """
        Check whether Ollama server is running.
        """
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )
            return response.status_code == 200

        except requests.RequestException:
            return False

    def list_models(self):
        """
        Return installed Ollama models.
        """
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            models = []

            for model in data.get("models", []):
                models.append(model["name"])

            return sorted(models)

        except requests.RequestException:
            return []

    def generate_response(
        self,
        prompt: str,
        model: str
    ):
        """
        Generate response from Ollama.
        """

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "top_p": 0.9,
                "num_predict": 8192,
                "repeat_penalty": 1.1
            }
        }

        try:

            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            print("DONE:", data.get("done"))
            print("DONE REASON:", data.get("done_reason"))
            print("EVAL COUNT:", data.get("eval_count"))

            return data.get("response", "")

        except requests.RequestException as error:

            return f"Error : {error}"