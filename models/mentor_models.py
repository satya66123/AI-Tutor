"""
AI Mentor Models
"""

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MentorGoal:

    id: Optional[int] = None

    title: str = ""

    description: str = ""

    category: str = ""

    target_value: int = 0

    current_value: int = 0

    progress: float = 0.0

    priority: str = "Medium"

    status: str = "Pending"

    due_date: Optional[date] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


@dataclass
class MentorProgress:

    id: Optional[int] = None

    study_date: Optional[date] = None

    study_hours: float = 0.0

    quizzes_completed: int = 0

    flashcards_completed: int = 0

    notes_created: int = 0

    coding_sessions: int = 0

    rag_queries: int = 0

    score: float = 0.0

    remarks: str = ""

    created_at: Optional[datetime] = None


@dataclass
class MentorRecommendation:

    id: Optional[int] = None

    recommendation_type: str = ""

    title: str = ""

    description: str = ""

    priority: str = "Medium"

    status: str = "Pending"

    created_at: Optional[datetime] = None


@dataclass
class MentorInsight:

    id: Optional[int] = None

    insight_type: str = ""

    title: str = ""

    description: str = ""

    generated_by: str = "AI Mentor"

    created_at: Optional[datetime] = None


@dataclass
class MentorSession:

    id: Optional[int] = None

    session_id: str = ""

    question: str = ""

    answer: str = ""

    provider: str = ""

    model: str = ""

    response_time: float = 0.0

    token_usage: int = 0

    created_at: Optional[datetime] = None