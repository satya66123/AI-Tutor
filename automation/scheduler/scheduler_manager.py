class SchedulerManager:

    def __init__(self):

        self.schedules = {}

    def add(self, schedule):

        self.schedules[schedule.schedule_id] = schedule

    def remove(self, schedule_id):

        self.schedules.pop(schedule_id, None)

    def get(self, schedule_id):

        return self.schedules.get(schedule_id)

    def get_all(self):

        return list(self.schedules.values())