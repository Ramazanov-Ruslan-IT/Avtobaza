from v1.src.app.services.schedule.abs_service import AbsScheduleService
from v1.src.db.repositories.schedule import AbsScheduleRepo
from v1.src.app.dto.schedule import ScheduleDTO


class ScheduleService(AbsScheduleService):
    def __init__(self, schedule_repo: AbsScheduleRepo):
        self.schedule_repo = schedule_repo

    async def create_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        return await self.schedule_repo.create_schedule(data)

    async def get_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        result = await self.schedule_repo.get_schedule(data)
        if not result:
            raise ValueError("Schedule not found")
        return result

    async def update_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        result = await self.schedule_repo.update_schedule(data)
        if not result:
            raise ValueError("Cannot update: schedule not found")
        return result

    async def delete_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        result = await self.schedule_repo.delete_schedule(data)
        if not result:
            raise ValueError("Cannot delete: schedule not found")
        return result
