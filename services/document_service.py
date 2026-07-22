"""
Enterprise RAG Document Service
"""

from pathlib import Path

import fitz
import docx
import pandas as pd


class DocumentService:

    @staticmethod
    def read(file):

        extension = Path(file.name).suffix.lower()

        if extension == ".pdf":
            return DocumentService.read_pdf(file)

        elif extension == ".docx":
            return DocumentService.read_docx(file)

        elif extension == ".txt":
            return file.read().decode("utf-8")

        elif extension == ".md":
            return file.read().decode("utf-8")

        elif extension == ".csv":
            return DocumentService.read_csv(file)

        elif extension == ".html":
            return file.read().decode("utf-8")

        elif extension in [
            ".py",
            ".java",
            ".js",
            ".php",
            ".cpp",
            ".c",
            ".cs"
        ]:
            return file.read().decode("utf-8")

        else:
            raise ValueError(f"Unsupported file : {extension}")

    @staticmethod
    def read_pdf(file):

        pdf = fitz.open(stream=file.read(), filetype="pdf")

        text = ""

        for page in pdf:

            text += page.get_text()

        return text

    @staticmethod
    def read_docx(file):

        document = docx.Document(file)

        return "\n".join(

            p.text

            for p in document.paragraphs

        )

    @staticmethod
    def read_csv(file):

        df = pd.read_csv(file)

        return df.to_string(index=False)