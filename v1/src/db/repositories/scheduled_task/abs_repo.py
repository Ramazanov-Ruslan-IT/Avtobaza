from abc import ABC, abstractmethod

from v1.src.app.dto.scheduled_task import ScheduledTaskDTO


class AbsScheduledTaskRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        raise NotImplementedError("create_scheduled_task() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        raise NotImplementedError("get_scheduled_task() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        raise NotImplementedError("update_scheduled_task() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_scheduled_task(cls, data: ScheduledTaskDTO) -> ScheduledTaskDTO | None | Exception:
        raise NotImplementedError("delete_scheduled_task() must be implemented in subclass")
