from dataclasses import dataclass, field

from automation.base_task import BaseTask
from automation.condition import Condition


@dataclass
class WorkflowStep:

    def __init__(self):
        self.name = None

    id: str

    task: BaseTask

    depends_on: list[str] = field(default_factory=list)

    conditions: list[Condition] = field(default_factory=list)

    enabled: bool = True