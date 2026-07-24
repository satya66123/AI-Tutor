from automation.tasks.notes_task import NotesTask
from automation.tasks.quiz_task import QuizTask
from automation.tasks.flashcard_task import FlashcardTask
from automation.tasks.analytics_task import AnalyticsTask


class TaskRegistry:

    _registry = {
        "notes": NotesTask,
        "quiz": QuizTask,
        "flashcards": FlashcardTask,
        "analytics": AnalyticsTask,
    }

    @classmethod
    def register(cls, name: str, task_class):
        cls._registry[name] = task_class

    @classmethod
    def get(cls, name: str):
        return cls._registry.get(name)

    @classmethod
    def list_tasks(cls):
        return list(cls._registry.keys())