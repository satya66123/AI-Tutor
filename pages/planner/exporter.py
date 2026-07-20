"""
Study Plan Exporter
"""

import streamlit as st


class PlannerExporter:

    @staticmethod
    def export(plan):

        st.download_button(
            "⬇ Download Plan",
            data=plan,
            file_name="study_plan.md",
            mime="text/markdown"
        )