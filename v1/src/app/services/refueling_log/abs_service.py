from abc import ABC, abstractmethod

from v1.src.app.dto.refueling_log import RefuelingLogDTO


class AbsRefuelingLogService(ABC):
    @abstractmethod
    async def create_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        pass

    @abstractmethod
    async def get_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        pass

    @abstractmethod
    async def update_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        pass
