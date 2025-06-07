from fastapi import Depends

from v1.src.app.services.role import build_role_service, AbsRoleService

async def get_role_service(
    role_service: AbsRoleService = Depends(build_role_service)
) -> AbsRoleService:
    return role_service
