"""
Application Health Check
"""

from services.provider_service import ProviderService


class HealthCheck:

    @staticmethod
    def run():

        return {

            "provider": ProviderService.is_provider_available()
        }