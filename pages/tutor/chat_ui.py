"""
Chat UI
"""

import streamlit as st

from pages.tutor.chat_history import ChatHistory
from pages.tutor.prompt_handler import PromptHandler
from pages.tutor.response_renderer import ResponseRenderer
from pages.tutor.stats import ChatStats
from services.chat_service import ChatService
from utils.error_handler import ErrorHandler



class ChatUI:

    @staticmethod
    def render(model):

        ChatHistory.initialize()

        for message in ChatHistory.get_messages():

            ResponseRenderer.render(
                message["role"],
                message["content"]
            )

        prompt = st.chat_input(
            "Ask your tutor..."
        )

        if prompt:

            prompt = PromptHandler.prepare(prompt)

            ChatHistory.add_user_message(prompt)

            ResponseRenderer.render(
                "user",
                prompt
            )

            with st.spinner("Thinking..."):

                try:

                    response = ChatService.generate_response(
                        prompt=prompt,
                        model=model
                    )

                except Exception as e:

                    ErrorHandler.handle(e)

                    return

            ChatHistory.add_assistant_message(response)

            ResponseRenderer.render(
                "assistant",
                response,
                stream=True
            )



            ####################################################
            # Show Statistics
            ####################################################



            ChatStats.render()
