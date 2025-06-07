from v1.src.app.services.refueling_log.abs_service import AbsRefuelingLogService
from v1.src.db.repositories.refueling_log import AbsRefuelingLogRepo
from v1.src.app.dto.refueling_log import RefuelingLogDTO


class RefuelingLogService(AbsRefuelingLogService):
    def __init__(self, refueling_log_repo: AbsRefuelingLogRepo):
        self.refueling_log_repo = refueling_log_repo

    async def create_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        return await self.refueling_log_repo.create_refueling_log(data)

    async def get_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        result = await self.refueling_log_repo.get_refueling_log(data)
        if not result:
            raise ValueError("Refueling log not found")
        return result

    async def update_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        result = await self.refueling_log_repo.update_refueling_log(data)
        if not result:
            raise ValueError("Cannot update: refueling log not found")
        return result

    async def delete_refueling_log(self, data: RefuelingLogDTO) -> RefuelingLogDTO | None | Exception:
        result = await self.refueling_log_repo.delete_refueling_log(data)
        if not result:
            raise ValueError("Cannot delete: refueling log not found")
        return result
