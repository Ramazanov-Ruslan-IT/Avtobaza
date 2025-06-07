from abc import ABC, abstractmethod

from v1.src.app.dto.access_log import AccessLogDTO


class AbsAccessLogService(ABC):
    @abstractmethod
    async def create_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        pass

    @abstractmethod
    async def get_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        pass

    @abstractmethod
    async def update_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_access_log(self, data: AccessLogDTO) -> AccessLogDTO | None | Exception:
        pass
