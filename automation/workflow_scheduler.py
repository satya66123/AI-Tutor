from uuid import uuid4



from automation.scheduler.schedule import Schedule
from automation.scheduler.schedule_type import ScheduleType
from automation.scheduler import SchedulerService


class WorkflowScheduler:

    def __init__(self, engine):

        self.scheduler = SchedulerService(engine)

    def schedule_once(self,
                      workflow,
                      run_time):



        schedule = Schedule(

            schedule_id=str(uuid4()),

            workflow_name=workflow,

            schedule_type=ScheduleType.ONCE,

            run_at=run_time

        )

        self.scheduler.add_schedule(schedule)

        return schedule