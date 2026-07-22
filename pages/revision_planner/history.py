"""
Planner History
"""

import streamlit as st


class PlannerHistory:

    @staticmethod
    def initialize():

        if "planner_history" not in st.session_state:

            st.session_state.planner_history = []

    @staticmethod
    def add(exam, subject):

        PlannerHistory.initialize()

        st.session_state.planner_history.append({

            "exam": exam,

            "subject": subject

        })

    @staticmethod
    def get():

        PlannerHistory.initialize()

        return st.session_state.planner_history