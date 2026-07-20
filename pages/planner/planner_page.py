"""
Planner Page
"""

from pages.planner.planner_ui import PlannerUI


class PlannerPage:

    @staticmethod
    def render(model):

        PlannerUI.render(model)