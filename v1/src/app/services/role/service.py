from v1.src.app.services.role.abs_service import AbsRoleService
from v1.src.db.repositories.role import AbsRoleRepo
from v1.src.app.dto.role import RoleDTO


class RoleService(AbsRoleService):
    def __init__(self, role_repo: AbsRoleRepo):
        self.role_repo = role_repo

    async def create_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        return await self.role_repo.create_role(data)

    async def get_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        result = await self.role_repo.get_role(data)
        if not result:
            raise ValueError("Role not found")
        return result

    async def update_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        result = await self.role_repo.update_role(data)
        if not result:
            raise ValueError("Cannot update: role not found")
        return result

    async def delete_role(self, data: RoleDTO) -> RoleDTO | None | Exception:
        result = await self.role_repo.delete_role(data)
        if not result:
            raise ValueError("Cannot delete: role not found")
        return result
