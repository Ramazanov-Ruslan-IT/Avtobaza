from v1.src.app.services.role.abs_service import AbsRoleService
from v1.src.app.services.role.service import RoleService

from v1.src.db.repositories.role.dependencies import get_role_repo


async def build_role_service() -> AbsRoleService:
    role_repo = await get_role_repo()
    return RoleService(role_repo)
