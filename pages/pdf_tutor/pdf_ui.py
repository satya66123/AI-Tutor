"""
PDF Tutor UI
"""

import streamlit as st

from pages.pdf_tutor.pdf_reader import PDFReader
from pages.pdf_tutor.chunker import TextChunker
from pages.pdf_tutor.pdf_service import PDFTutorService
from pages.pdf_tutor.exporter import PDFExporter
from pages.pdf_tutor.analytics import PDFAnalytics
from pages.pdf_tutor.history import PDFHistory
from pages.pdf_tutor.models import CHUNK_SIZES

from services.model_service import ModelService
from utils.error_handler import ErrorHandler


class PDFTutorUI:

    @staticmethod
    def initialize():

        defaults = {
            "pdf_text": "",
            "pdf_chunks": [],
            "pdf_answer": "",
            "pdf_loaded": False,
            "pdf_name": None
        }

        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @staticmethod
    def render():

        PDFTutorUI.initialize()

        st.title("📄 AI PDF Tutor")
        st.write("Upload a PDF and ask questions about it.")

        st.divider()

        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"]
        )

        chunk_size = st.selectbox(
            "Chunk Size",
            CHUNK_SIZES,
            index=1
        )

        models = ModelService.get_models()

        model = st.selectbox(
            "AI Model",
            models
        )

        ####################################################
        # Load PDF ONLY ONCE
        ####################################################

        if uploaded_file:

            if (
                not st.session_state.pdf_loaded
                or st.session_state.pdf_name != uploaded_file.name
            ):

                try:

                    with st.spinner("Reading PDF..."):

                        text = PDFReader.extract_text(uploaded_file)

                        chunks = TextChunker.split(
                            text,
                            chunk_size
                        )

                    st.session_state.pdf_text = text
                    st.session_state.pdf_chunks = chunks
                    st.session_state.pdf_loaded = True
                    st.session_state.pdf_name = uploaded_file.name

                    PDFHistory.add(uploaded_file.name)

                    st.success("✅ PDF Loaded Successfully")

                except Exception as e:

                    ErrorHandler.handle(e)
                    return

        ####################################################
        # Show Statistics
        ####################################################

        if st.session_state.pdf_loaded:

            st.info(f"📄 {st.session_state.pdf_name}")



            question = st.text_input(
                "Ask a Question"
            )

            if st.button(
                "🚀 Ask AI",
                use_container_width=True
            ):

                if not question.strip():

                    st.warning("Please enter a question.")
                    st.stop()

                if not st.session_state.pdf_text:

                    st.error("PDF text is empty.")
                    st.stop()

                if not st.session_state.pdf_chunks:

                    st.error("PDF chunks are empty.")
                    st.stop()

                try:

                    with st.spinner("Thinking..."):

                        context = "\n\n".join(
                            st.session_state.pdf_chunks
                        )

                        answer = PDFTutorService.ask(

                            context=context,

                            question=question,

                            model=model

                        )

                    st.session_state.pdf_answer = answer





                except Exception as e:

                    ErrorHandler.handle(e)

            if st.session_state.pdf_answer:

                st.divider()

                st.subheader("🤖 AI Answer")

                st.markdown(
                    st.session_state.pdf_answer
                )

                st.session_state.pdf_questions += 1
                st.session_state.pdf_answers += 1

                PDFAnalytics.render(
                    st.session_state.pdf_text,
                    st.session_state.pdf_chunks
                )

                st.divider()

                PDFExporter.download(
                    st.session_state.pdf_answer
                )

        ####################################################
        # History
        ####################################################

        st.divider()

        if st.checkbox("Show PDF History"):

            history = PDFHistory.get()

            if history:

                for pdf in reversed(history):

                    st.write("📄", pdf)

            else:

                st.info("No PDFs uploaded.")

        ####################################################
        # Clear
        ####################################################

        st.divider()

        if st.button(
            "🗑 Clear PDF",
            use_container_width=True
        ):

            st.session_state.pdf_text = ""
            st.session_state.pdf_chunks = []
            st.session_state.pdf_answer = ""
            st.session_state.pdf_loaded = False
            st.session_state.pdf_name = None
            st.session_state.pdf_text = ""
            st.session_state.pdf_chunks = []
            st.session_state.pdf_answer = ""
            st.session_state.pdf_loaded = False
            st.session_state.pdf_name = None
            st.session_state.pdf_questions = 0
            st.session_state.pdf_answers = 0

            st.rerun()