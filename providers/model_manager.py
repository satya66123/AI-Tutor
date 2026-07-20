"""
Model Manager
"""

from providers.provider_factory import ProviderFactory


class ModelManager:
    """
    Handles model management across providers.
    """

    # Default Model
    DEFAULT_MODEL = "qwen2.5:1.5b"

    # Models we don't want to display
    EXCLUDED_MODELS = {
        "nomic-embed-text:latest",
        "mxbai-embed-large:latest",
        "translategemma:12b",
        "deepseek-v3.1:671b-cloud",
        "glm-4.6:cloud",
        "minimax-m2:cloud",
        "qwen3-vl:235b-cloud",
        "qwen3-coder:480b-cloud",
        "gpt-oss:120b-cloud",
        "llama3:latest",
        "llama3:instruct",
        "qwen3:latest",
    }

    @staticmethod
    def get_models():
        """
        Return filtered models.
        """

        provider = ProviderFactory.get_provider()

        models = provider.list_models()

        filtered_models = []

        for model in models:

            if model in ModelManager.EXCLUDED_MODELS:
                continue

            filtered_models.append(model)

        return sorted(filtered_models)

    @staticmethod
    def get_default_model():
        """
        Return the default model.
        """

        models = ModelManager.get_models()

        if ModelManager.DEFAULT_MODEL in models:
            return ModelManager.DEFAULT_MODEL

        if models:
            return models[0]

        return None