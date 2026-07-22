"""
Coding Tutor History
"""

import streamlit as st


class CodingHistory:

    @staticmethod
    def initialize():

        if "coding_history" not in st.session_state:

            st.session_state.coding_history = []

    @staticmethod
    def add(task, language):

        CodingHistory.initialize()

        st.session_state.coding_history.append({

            "task": task,

            "language": language

        })

    @staticmethod
    def get():

        CodingHistory.initialize()

        return st.session_state.coding_history