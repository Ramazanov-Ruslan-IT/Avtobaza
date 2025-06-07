from abc import ABC, abstractmethod

from v1.src.app.dto.schedule import ScheduleDTO


class AbsScheduleRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        raise NotImplementedError("create_schedule() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        raise NotImplementedError("get_schedule() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        raise NotImplementedError("update_schedule() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_schedule(cls, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        raise NotImplementedError("delete_schedule() must be implemented in subclass")
