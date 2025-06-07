from v1.src.db.repositories.autobase.repo import AutobaseRepo
from v1.src.db.repositories.autobase.abs_repo import AbsAutobaseRepo


async def get_autobase_repo() -> AbsAutobaseRepo:
    return AutobaseRepo()
