from abc import ABC, abstractmethod

from v1.src.app.dto.access_log import AccessLogDTO


class AbsAccessLogRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        raise NotImplementedError("create_access_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        raise NotImplementedError("get_access_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        raise NotImplementedError("update_access_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_access_log(cls, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        raise NotImplementedError("delete_access_log() must be implemented in subclass")
