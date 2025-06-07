from v1.src.db.repositories.scheduled_task.repo import ScheduledTaskRepo
from v1.src.db.repositories.scheduled_task.abs_repo import AbsScheduledTaskRepo


async def get_scheduled_task_repo() -> AbsScheduledTaskRepo:
    return ScheduledTaskRepo()
