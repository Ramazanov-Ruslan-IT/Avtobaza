from abc import ABC, abstractmethod

from v1.src.app.dto.system_event import SystemEventDTO


class AbsSystemEventRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_system_event(cls, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        raise NotImplementedError("create_system_event() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_system_event(cls, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        raise NotImplementedError("get_system_event() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_system_event(cls, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        raise NotImplementedError("update_system_event() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_system_event(cls, data: SystemEventDTO) -> SystemEventDTO | None | Exception:
        raise NotImplementedError("delete_system_event() must be implemented in subclass")
