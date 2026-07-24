from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict

from automation.task_status import TaskStatus


@dataclass
class Task:

    task_id: str

    task_name: str

    task_type: str

    input_data: Dict[str, Any] = field(default_factory=dict)

    output_data: Dict[str, Any] = field(default_factory=dict)

    status: TaskStatus = TaskStatus.PENDING

    started_at: datetime | None = None

    completed_at: datetime | None = None

    error: str | None = None