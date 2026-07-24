from abc import ABC, abstractmethod


class Scheduler(ABC):

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def add_schedule(self, schedule):
        ...

    @abstractmethod
    def remove_schedule(self, schedule_id):
        ...

    @abstractmethod
    def run_pending(self):
        ...