from v1.src.db.repositories.repair_request.repo import RepairRequestRepo
from v1.src.db.repositories.repair_request.abs_repo import AbsRepairRequestRepo


async def get_repair_request_repo() -> AbsRepairRequestRepo:
    return RepairRequestRepo()
