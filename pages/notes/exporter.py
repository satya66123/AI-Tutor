"""
Notes Exporter
"""

import streamlit as st


class NotesExporter:

    @staticmethod
    def download(notes):

        st.download_button(

            "📥 Download Notes",

            notes,

            file_name="notes.txt",

            mime="text/plain"

        )