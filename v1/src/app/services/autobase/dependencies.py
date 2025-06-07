from v1.src.app.services.autobase.abs_service import AbsAutobaseService
from v1.src.app.services.autobase.service import AutobaseService

from v1.src.db.repositories.autobase.dependencies import get_autobase_repo


async def build_autobase_service() -> AbsAutobaseService:
    autobase_repo = await get_autobase_repo()
    return AutobaseService(autobase_repo)
