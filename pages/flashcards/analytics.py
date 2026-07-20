"""
Flashcards Analytics
"""

import streamlit as st


class FlashcardsAnalytics:

    @staticmethod
    def render(cards):

        st.subheader("📊 Statistics")

        st.metric(
            "Total Flashcards",
            len(cards)
        )

        total_front = sum(
            len(card["front"])
            for card in cards
        )

        total_back = sum(
            len(card["back"])
            for card in cards
        )

        st.metric(
            "Average Front Length",
            round(total_front / len(cards), 1)
            if cards else 0
        )

        st.metric(
            "Average Back Length",
            round(total_back / len(cards), 1)
            if cards else 0
        )