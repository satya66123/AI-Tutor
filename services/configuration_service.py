"""
Configuration Validation Service
"""

from config.config import Config


class ConfigurationService:

    @staticmethod
    def validate():

        errors = []

        if not Config.MYSQL_HOST:
            errors.append("MYSQL_HOST missing")

        if not Config.MYSQL_DATABASE:
            errors.append("MYSQL_DATABASE missing")

        if not Config.OLLAMA_HOST:
            errors.append("OLLAMA_HOST missing")

        return {

            "valid": len(errors) == 0,

            "errors": errors

        }