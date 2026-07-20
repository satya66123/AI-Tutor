"""
Flashcards Exporter
"""

import streamlit as st
import json


class FlashcardsExporter:

    @staticmethod
    def download_txt(cards):

        text = ""

        for index, card in enumerate(cards, start=1):

            text += f"Flashcard {index}\n"
            text += f"Front: {card['front']}\n"
            text += f"Back : {card['back']}\n\n"

        st.download_button(

            "📥 Download TXT",

            text,

            file_name="flashcards.txt",

            mime="text/plain"

        )

    @staticmethod
    def download_json(cards):

        st.download_button(

            "📥 Download JSON",

            json.dumps(cards, indent=4),

            file_name="flashcards.json",

            mime="application/json"

        )