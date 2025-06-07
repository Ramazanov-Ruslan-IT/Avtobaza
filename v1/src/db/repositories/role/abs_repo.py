from abc import ABC, abstractmethod

from v1.src.app.dto.role import RoleDTO


class AbsRoleRepo(ABC):
    @classmethod
    @abstractmethod
    async def create_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        raise NotImplementedError("create_role() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def get_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        raise NotImplementedError("get_role() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def update_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        raise NotImplementedError("update_role() must be implemented in subclass")

    @classmethod
    @abstractmethod
    async def delete_role(cls, data: RoleDTO) -> RoleDTO | None | Exception:
        raise NotImplementedError("delete_role() must be implemented in subclass")
