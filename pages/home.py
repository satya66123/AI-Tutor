"""
Home Page
"""

import streamlit as st


class HomePage:

    @staticmethod
    def render():

        st.subheader("🏠 Home")

        st.write(
            """
Welcome to AI Tutor.

Features

• AI Chat

• Study Planner

• Quiz Generator

• Coding Tutor

• PDF Tutor

• Voice Tutor
"""
        )