"""
Interview Preparation Models
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class InterviewQuestion:

    id: Optional[int] = None

    category: str = ""

    difficulty: str = "Easy"

    question: str = ""

    answer: str = ""

    tags: str = ""

    created_at: Optional[datetime] = None


@dataclass
class InterviewSession:

    id: Optional[int] = None

    session_id: str = ""

    interview_type: str = ""

    provider: str = ""

    model: str = ""

    started_at: Optional[datetime] = None

    completed_at: Optional[datetime] = None


@dataclass
class InterviewAnswer:

    id: Optional[int] = None

    session_id: str = ""

    question: str = ""

    user_answer: str = ""

    ai_feedback: str = ""

    score: float = 0.0

    created_at: Optional[datetime] = None


@dataclass
class InterviewReport:

    id: Optional[int] = None

    session_id: str = ""

    overall_score: float = 0.0

    strengths: str = ""

    weaknesses: str = ""

    recommendations: str = ""

    created_at: Optional[datetime] = None


@dataclass
class InterviewHistory:

    id: Optional[int] = None

    session_id: str = ""

    interview_type: str = ""

    total_questions: int = 0

    score: float = 0.0

    duration: float = 0.0

    provider: str = ""

    model: str = ""

    created_at: Optional[datetime] = None