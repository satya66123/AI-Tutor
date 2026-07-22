"""
Revision Planner Exporter
"""

import streamlit as st


class PlannerExporter:

    @staticmethod
    def download(plan):

        st.download_button(

            "📥 Download Plan",

            plan,

            file_name="revision_plan.txt",

            mime="text/plain"

        )