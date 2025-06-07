from v1.src.app.services.system_event.abs_service import AbsSystemEventService
from v1.src.db.repositories.system_event import AbsSystemEventRepo
from v1.src.app.dto.system_event import SystemEventDTO


class SystemEventService(AbsSystemEventService):
    def __init__(self, system_event_repo: AbsSystemEventRepo):
        self.system_event_repo = system_event_repo

    async def create_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        return await self.system_event_repo.create_system_event(data)

    async def get_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        result = await self.system_event_repo.get_system_event(data)
        if not result:
            raise ValueError("System event not found")
        return result

    async def update_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        result = await self.system_event_repo.update_system_event(data)
        if not result:
            raise ValueError("Cannot update: system event not found")
        return result

    async def delete_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        result = await self.system_event_repo.delete_system_event(data)
        if not result:
            raise ValueError("Cannot delete: system event not found")
        return result
