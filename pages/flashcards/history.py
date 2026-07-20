"""
Flashcards History
"""

import streamlit as st


class FlashcardsHistory:

    @staticmethod
    def initialize():

        if "flashcards_history" not in st.session_state:

            st.session_state.flashcards_history = []

    @staticmethod
    def add(topic, cards):

        FlashcardsHistory.initialize()

        st.session_state.flashcards_history.append({

            "topic": topic,
            "cards": cards

        })

    @staticmethod
    def get():

        FlashcardsHistory.initialize()

        return st.session_state.flashcards_history