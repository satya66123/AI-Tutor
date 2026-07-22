"""
Learning Analytics Page
"""

from pages.analytics.analytics_ui import (
    LearningAnalyticsUI
)


class AnalyticsPage:

    @staticmethod
    def render():

        LearningAnalyticsUI.render()