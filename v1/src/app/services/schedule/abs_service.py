from abc import ABC, abstractmethod

from v1.src.app.dto.schedule import ScheduleDTO


class AbsScheduleService(ABC):
    @abstractmethod
    async def create_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        pass

    @abstractmethod
    async def get_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        pass

    @abstractmethod
    async def update_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_schedule(self, data: ScheduleDTO) -> ScheduleDTO | None | Exception:
        pass
