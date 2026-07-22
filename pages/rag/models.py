"""
Enterprise RAG Models
"""

from enum import Enum


class ChunkStrategy(Enum):

    FIXED = "Fixed"

    RECURSIVE = "Recursive"

    SEMANTIC = "Semantic"

    PARENT_CHILD = "Parent Child"

    SLIDING_WINDOW = "Sliding Window"

    TOKEN = "Token"

    STRUCTURE = "Structure"


class EmbeddingProvider(Enum):

    OLLAMA = "Ollama"

    OPENAI = "OpenAI"

    HUGGINGFACE = "HuggingFace"


class SearchType(Enum):

    SEMANTIC = "Semantic"

    KEYWORD = "Keyword"

    HYBRID = "Hybrid"

    REWRITE = "Rewrite"

    MULTI_QUERY = "Multi Query"

    HYDE = "HyDE"

    PARENT_CHILD = "Parent Child"



class RetrievalStrategy(Enum):

    STANDARD = "Standard"

    MULTI_QUERY = "Multi Query"

    HYDE = "HyDE"

    PARENT_CHILD = "Parent Child"


SUPPORTED_FILES = [

    "pdf",

    "docx",

    "txt",

    "md",

    "csv",

    "html",

    "py",

    "java",

    "js",

    "php",

    "cpp",

    "c",

    "cs"

]

TOP_K_VALUES = [

    3,

    5,

    10,

    15,

    20

]

CHUNK_SIZES = [

    256,

    512,

    768,

    1024,

    2048

]

OVERLAP_SIZES = [

    0,

    50,

    100,

    150,

    200

]

RERANK_TOP_K = [

    5,

    10,

    20

]