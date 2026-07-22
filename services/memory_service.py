"""
Conversation Memory Service
"""

import streamlit as st


class MemoryService:

    @staticmethod
    def initialize():

        if "rag_memory" not in st.session_state:

            st.session_state.rag_memory = []

    @staticmethod
    def add(question, answer):

        MemoryService.initialize()

        st.session_state.rag_memory.append({

            "question": question,

            "answer": answer

        })

    @staticmethod
    def get_context(max_turns=5):

        MemoryService.initialize()

        history = st.session_state.rag_memory[-max_turns:]

        context = ""

        for item in history:

            context += f"""
User:
{item['question']}

Assistant:
{item['answer']}

"""

        return context

    @staticmethod
    def clear():

        st.session_state.rag_memory = []