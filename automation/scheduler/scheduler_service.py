from datetime import datetime
import time

from automation.scheduler.scheduler import Scheduler
from automation.scheduler.scheduler_manager import SchedulerManager


class SchedulerService(Scheduler):

    def __init__(self, workflow_engine):

        self.workflow_engine = workflow_engine

        self.manager = SchedulerManager()

        self.running = False

    def start(self):

        self.running = True

        while self.running:

            self.run_pending()

            time.sleep(1)

    def stop(self):

        self.running = False

    def add_schedule(self, schedule):

        self.manager.add(schedule)

    def remove_schedule(self, schedule_id):

        self.manager.remove(schedule_id)

    def run_pending(self):

        now = datetime.now()

        for schedule in self.manager.get_all():

            if not schedule.enabled:
                continue

            if schedule.run_at is None:
                continue

            if now >= schedule.run_at:

                print(
                    f"Executing {schedule.workflow_name}"
                )

                schedule.enabled = False
                schedule.enabled = False