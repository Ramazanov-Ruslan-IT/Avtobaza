from abc import ABC, abstractmethod

from v1.src.app.dto.system_event import SystemEventDTO


class AbsSystemEventService(ABC):
    @abstractmethod
    async def create_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        pass

    @abstractmethod
    async def get_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        pass

    @abstractmethod
    async def update_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_system_event(self, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        pass
