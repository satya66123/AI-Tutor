"""
Coding Exporter
"""

import streamlit as st


class CodingExporter:

    @staticmethod
    def download(result):

        st.download_button(

            "📥 Download Result",

            result,

            file_name="coding_tutor.txt",

            mime="text/plain"

        )