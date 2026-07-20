"""
Model Service
"""

from providers.model_manager import ModelManager


class ModelService:
    """
    Service for model operations.
    """

    @staticmethod
    def get_models():
        return ModelManager.get_models()

    @staticmethod
    def get_default_model():
        return ModelManager.get_default_model()