from enum import Enum


class ScheduleType(Enum):

    ONCE = "once"

    DELAY = "delay"

    DAILY = "daily"

    WEEKLY = "weekly"

    MONTHLY = "monthly"

    CRON = "cron"