from fastapi import Depends

from v1.src.app.services.scheduled_task import build_scheduled_task_service, AbsScheduledTaskService

async def get_scheduled_task_service(
    scheduled_task_service: AbsScheduledTaskService = Depends(build_scheduled_task_service)
) -> AbsScheduledTaskService:
    return scheduled_task_service
