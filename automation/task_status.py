from enum import Enum


class TaskStatus(Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    SKIPPED = "Skipped"