from v1.src.db.repositories.role.repo import RoleRepo
from v1.src.db.repositories.role.abs_repo import AbsRoleRepo


async def get_role_repo() -> AbsRoleRepo:
    return RoleRepo()
