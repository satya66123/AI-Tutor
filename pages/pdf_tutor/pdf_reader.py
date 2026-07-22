"""
PDF Reader
"""

import fitz  # PyMuPDF


class PDFReader:

    @staticmethod
    def extract_text(file):

        try:

            pdf = fitz.open(stream=file.read(), filetype="pdf")

            text = ""

            for page in pdf:

                page_text = page.get_text("text")

                if page_text:
                    text += page_text + "\n"

            pdf.close()

            return text.strip()

        except Exception as e:

            raise Exception(f"Error reading PDF: {str(e)}")