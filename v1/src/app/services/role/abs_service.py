from abc import ABC, abstractmethod

from v1.src.app.dto.role import RoleDTO


class AbsRoleService(ABC):
    @abstractmethod
    async def create_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        pass

    @abstractmethod
    async def get_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        pass

    @abstractmethod
    async def update_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        pass

    @abstractmethod
    async def delete_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        pass
