"""
Enterprise RAG Exporter
"""

import json
import streamlit as st


class RAGExporter:

    @staticmethod
    def export_answer(question, answer):

        text = f"""

Question
========

{question}


Answer
======

{answer}

"""

        st.download_button(

            label="📥 Download Answer",

            data=text,

            file_name="rag_answer.txt",

            mime="text/plain"

        )

    @staticmethod
    def export_history(history):

        st.download_button(

            label="📥 Export History",

            data=json.dumps(

                history,

                indent=4,

                default=str

            ),

            file_name="rag_history.json",

            mime="application/json"

        )