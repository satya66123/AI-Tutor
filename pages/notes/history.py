"""
Notes History
"""

import streamlit as st


class NotesHistory:

    @staticmethod
    def initialize():

        if "notes_history" not in st.session_state:

            st.session_state.notes_history = []

    @staticmethod
    def add(notes):

        NotesHistory.initialize()

        st.session_state.notes_history.append(notes)

    @staticmethod
    def get():

        NotesHistory.initialize()

        return st.session_state.notes_history