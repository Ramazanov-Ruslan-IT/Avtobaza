from fastapi import Depends

from v1.src.app.services.schedule import build_schedule_service, AbsScheduleService

async def get_schedule_service(
    schedule_service: AbsScheduleService = Depends(build_schedule_service)
) -> AbsScheduleService:
    return schedule_service
