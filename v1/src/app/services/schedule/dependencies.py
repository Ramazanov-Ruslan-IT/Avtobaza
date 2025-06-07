from v1.src.app.services.schedule.abs_service import AbsScheduleService
from v1.src.app.services.schedule.service import ScheduleService

from v1.src.db.repositories.schedule.dependencies import get_schedule_repo


async def build_schedule_service() -> AbsScheduleService:
    schedule_repo = await get_schedule_repo()
    return ScheduleService(schedule_repo)
