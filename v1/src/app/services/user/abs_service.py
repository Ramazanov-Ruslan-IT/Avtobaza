from abc import ABC, abstractmethod

from v1.src.app.dto.user import UserDTO


class AbsUserService(ABC):
    @abstractmethod
    async def create_user(self, data: UserDTO) -> UserDTO | None | Exception:
        pass

    @abstractmethod
    async def get_user(self, data: UserDTO) -> UserDTO | None | Exception:
        pass

    @abstractmethod
    async def update_user(self, data: UserDTO) -> UserDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_user(self, data: UserDTO) -> UserDTO | None | Exception:
        pass
