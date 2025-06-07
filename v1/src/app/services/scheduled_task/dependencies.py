from v1.src.app.services.scheduled_task.abs_service import AbsScheduledTaskService
from v1.src.app.services.scheduled_task.service import ScheduledTaskService

from v1.src.db.repositories.scheduled_task.dependencies import get_scheduled_task_repo


async def build_scheduled_task_service() -> AbsScheduledTaskService:
    scheduled_task_repo = await get_scheduled_task_repo()
    return ScheduledTaskService(scheduled_task_repo)
