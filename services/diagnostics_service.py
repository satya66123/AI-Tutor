"""
Enterprise Diagnostics
"""

from services.cache_service import CacheService
from services.configuration_service import ConfigurationService
from services.health_check_service import HealthCheckService


class DiagnosticsService:

    @staticmethod
    def report():

        config = ConfigurationService.validate()

        health = HealthCheckService.check()

        return {

            "configuration": config,

            "health": health,

            "cache_entries": CacheService.size()

        }