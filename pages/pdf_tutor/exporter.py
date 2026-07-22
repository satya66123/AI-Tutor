"""
PDF Exporter
"""

import streamlit as st


class PDFExporter:

    @staticmethod
    def download(chat):

        st.download_button(

            "📥 Download Chat",

            chat,

            file_name="pdf_chat.txt",

            mime="text/plain"

        )