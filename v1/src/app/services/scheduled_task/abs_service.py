from abc import ABC, abstractmethod

from v1.src.app.dto.scheduled_task import ScheduledTaskDTO


class AbsScheduledTaskService(ABC):
    @abstractmethod
    async def create_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        pass

    @abstractmethod
    async def get_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        pass

    @abstractmethod
    async def update_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_scheduled_task(self, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        pass
