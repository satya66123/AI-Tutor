"""
Enterprise RAG History
"""

import streamlit as st
from datetime import datetime


class RAGHistory:

    @staticmethod
    def initialize():

        if "rag_history" not in st.session_state:

            st.session_state.rag_history = []

    @staticmethod
    def add(question, answer, sources):

        RAGHistory.initialize()

        st.session_state.rag_history.append({

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "question": question,

            "answer": answer,

            "sources": sources

        })

    @staticmethod
    def get():

        RAGHistory.initialize()

        return st.session_state.rag_history

    @staticmethod
    def clear():

        st.session_state.rag_history = []