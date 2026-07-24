from dataclasses import dataclass
from datetime import datetime

from automation.scheduler.schedule_type import ScheduleType


@dataclass
class Schedule:

    schedule_id: str

    workflow_name: str

    schedule_type: ScheduleType

    run_at: datetime | None = None

    cron: str | None = None

    enabled: bool = True