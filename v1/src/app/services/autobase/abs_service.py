from abc import ABC, abstractmethod

from v1.src.app.dto.autobase import AutobaseDTO


class AbsAutobaseService(ABC):
    @abstractmethod
    async def create_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        pass

    @abstractmethod
    async def get_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        pass

    @abstractmethod
    async def update_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        pass
