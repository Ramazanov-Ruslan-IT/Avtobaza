from abc import ABC, abstractmethod

from v1.src.app.dto.user import UserDTO


class AbsUserRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        raise NotImplementedError("create_user() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        raise NotImplementedError("get_user() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        raise NotImplementedError("update_user() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_user(cls, data: UserDTO) -> UserDTO | None | Exception:
        raise NotImplementedError("delete_user() must be implemented in subclass")
