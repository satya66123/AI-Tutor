"""
Voice AI Tutor Models
"""

from dataclasses import dataclass
from typing import Optional


# =====================================================
# Voice Session
# =====================================================

@dataclass
class VoiceSession:

    session_id: str

    provider: str

    model: str

    language: str = "en"

    status: str = "Active"

    started_at: Optional[str] = None

    ended_at: Optional[str] = None

    total_messages: int = 0

    total_duration: float = 0.0

    created_at: Optional[str] = None


# =====================================================
# Voice Message
# =====================================================

@dataclass
class VoiceMessage:

    session_id: str

    sender: str

    transcript: str

    response: str = ""

    audio_file: str = ""

    response_time: float = 0.0

    token_usage: int = 0

    created_at: Optional[str] = None


# =====================================================
# Voice History
# =====================================================

@dataclass
class VoiceHistory:

    session_id: str

    transcript: str

    ai_response: str

    provider: str

    model: str

    language: str

    created_at: Optional[str] = None


# =====================================================
# Voice Settings
# =====================================================

@dataclass
class VoiceSettings:

    language: str = "en"

    voice: str = "default"

    speech_rate: float = 1.0

    pitch: float = 1.0

    provider: str = "Ollama"

    model: str = "qwen2.5:1.5b"

    updated_at: Optional[str] = None


# =====================================================
# Voice Analytics
# =====================================================

@dataclass
class VoiceAnalytics:

    session_id: str

    total_duration: float = 0.0

    speaking_duration: float = 0.0

    ai_duration: float = 0.0

    total_messages: int = 0

    average_response_time: float = 0.0

    provider: str = ""

    model: str = ""

    created_at: Optional[str] = None