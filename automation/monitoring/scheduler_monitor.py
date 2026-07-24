class SchedulerMonitor:

    def __init__(self, persistence):

        self.persistence = persistence

    def get_schedules(self):

        repos = self.persistence.repositories()

        return repos.schedules.find_active()

    def get_schedule(self, schedule_id):

        repos = self.persistence.repositories()

        return repos.schedules.find(schedule_id)