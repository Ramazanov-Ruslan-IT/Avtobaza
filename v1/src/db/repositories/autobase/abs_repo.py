from abc import ABC, abstractmethod

from v1.src.app.dto.autobase import AutobaseDTO


class AbsAutobaseRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        raise NotImplementedError("create_autobase() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        raise NotImplementedError("get_autobase() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        raise NotImplementedError("update_autobase() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_autobase(cls, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        raise NotImplementedError("delete_autobase() must be implemented in subclass")
