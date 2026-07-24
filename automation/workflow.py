from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from automation.workflow_status import WorkflowStatus
from automation.workflow_step import WorkflowStep


if TYPE_CHECKING:
    from automation.base_task import BaseTask


@dataclass
class Workflow:

    workflow_id: str

    workflow_name: str

    description: str

    tasks: list["BaseTask"] = field(default_factory=list)

    steps: list[WorkflowStep] = field(default_factory=list)


    status: WorkflowStatus = WorkflowStatus.PENDING

    results: dict = field(default_factory=dict)