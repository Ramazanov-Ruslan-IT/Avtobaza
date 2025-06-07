from v1.src.app.services.scheduled_task.abs_service import AbsScheduledTaskService
from v1.src.db.repositories.scheduled_task import AbsScheduledTaskRepo
from v1.src.app.dto.scheduled_task import ScheduledTaskDTO


class ScheduledTaskService(AbsScheduledTaskService):
    def __init__(self, scheduled_task_repo: AbsScheduledTaskRepo):
        self.scheduled_task_repo = scheduled_task_repo

    async def create_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        return await self.scheduled_task_repo.create_scheduled_task(data)

    async def get_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        result = await self.scheduled_task_repo.get_scheduled_task(data)
        if not result:
            raise ValueError("Scheduled task not found")
        return result

    async def update_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        result = await self.scheduled_task_repo.update_scheduled_task(data)
        if not result:
            raise ValueError("Cannot update: scheduled task not found")
        return result

    async def delete_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        result = await self.scheduled_task_repo.delete_scheduled_task(data)
        if not result:
            raise ValueError("Cannot delete: scheduled task not found")
        return result
