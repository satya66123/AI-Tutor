"""
Configuration settings for the AI Tutor application.
Loads environment variables from the .env file.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # ==========================
    # Application
    # ==========================
    APP_NAME = "AI Tutor"
    APP_VERSION = "1.0.0"

    # ==========================
    # MySQL
    # ==========================
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "ai_tutor")

    # ==========================
    # Default Provider
    # ==========================
    DEFAULT_PROVIDER = os.getenv("PROVIDER", "ollama")

    # ==========================
    # Ollama
    # ==========================
    OLLAMA_HOST = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

    # Default Embedding Model
    OLLAMA_EMBEDDING_MODEL = os.getenv(
        "OLLAMA_EMBEDDING_MODEL",
        "nomic-embed-text"
    )

    # ==========================
    # OpenAI
    # ==========================
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )

    OPENAI_EMBEDDING_MODEL = os.getenv(
        "OPENAI_EMBEDDING_MODEL",
        "text-embedding-3-small"
    )

    # ==========================
    # Anthropic
    # ==========================
    ANTHROPIC_API_KEY = os.getenv(
        "ANTHROPIC_API_KEY",
        ""
    )

    # ==========================
    # FAISS
    # ==========================
    FAISS_INDEX_PATH = os.getenv(
        "FAISS_INDEX_PATH",
        "data/faiss/index.faiss"
    )

    FAISS_METADATA_PATH = os.getenv(
        "FAISS_METADATA_PATH",
        "data/faiss/metadata.pkl"
    )

    # ==========================
    # RAG
    # ==========================
    DEFAULT_CHUNK_SIZE = 512

    DEFAULT_CHUNK_OVERLAP = 100

    DEFAULT_TOP_K = 5

    MAX_UPLOAD_SIZE_MB = 100