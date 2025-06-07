from v1.src.db.repositories.schedule.repo import ScheduleRepo
from v1.src.db.repositories.schedule.abs_repo import AbsScheduleRepo


async def get_schedule_repo() -> AbsScheduleRepo:
    return ScheduleRepo()
