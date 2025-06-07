from v1.src.app.services.autobase.abs_service import AbsAutobaseService
from v1.src.db.repositories.autobase import AbsAutobaseRepo
from v1.src.app.dto.autobase import AutobaseDTO


class AutobaseService(AbsAutobaseService):
    def __init__(self, autobase_repo: AbsAutobaseRepo):
        self.autobase_repo = autobase_repo

    async def create_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        return await self.autobase_repo.create_autobase(data)

    async def get_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        result = await self.autobase_repo.get_autobase(data)
        if not result:
            raise ValueError("Autobase not found")
        return result

    async def update_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        result = await self.autobase_repo.update_autobase(data)
        if not result:
            raise ValueError("Cannot update: autobase not found")
        return result

    async def delete_autobase(self, data: AutobaseDTO) -> AutobaseDTO | None | Exception:
        result = await self.autobase_repo.delete_autobase(data)
        if not result:
            raise ValueError("Cannot delete: autobase not found")
        return result
