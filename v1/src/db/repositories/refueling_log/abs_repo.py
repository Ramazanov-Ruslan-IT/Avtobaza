from abc import ABC, abstractmethod

from v1.src.app.dto.refueling_log import RefuelingLogDTO


class AbsRefuelingLogRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        raise NotImplementedError("create_refueling_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        raise NotImplementedError("get_refueling_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        raise NotImplementedError("update_refueling_log() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_refueling_log(cls, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        raise NotImplementedError("delete_refueling_log() must be implemented in subclass")
