"""
Notes Analytics
"""

import streamlit as st


class NotesAnalytics:

    @staticmethod
    def render(notes):

        words = len(notes.split())

        characters = len(notes)

        st.subheader("📊 Notes Statistics")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Words",

                words

            )

        with col2:

            st.metric(

                "Characters",

                characters

            )