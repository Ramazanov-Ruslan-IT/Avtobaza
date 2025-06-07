from fastapi import Depends, Body, APIRouter, Query, Path

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.repair_request.dependencies import get_repair_request_service, AbsRepairRequestService
from v1.src.app.dto.repair_request import RepairRequestDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.repair_request.schemas import (
    RepairRequestCreateSchema, RepairRequestGetSchema, RepairRequestUpdateSchema, RepairRequestDeleteSchema,
    RepairRequestResponseSchema1, RepairRequestResponseSchema2, RepairRequestResponseSchema3, RepairRequestResponseSchema4,
    RepairRequestListSchema, RepairRequestBatchStatusSchema, RepairRequestBatchStatusResponseSchema,
    RepairRequestHistoryListSchema, RepairRequestStatsSchema
)

router = APIRouter(prefix="/repair_request", tags=["RepairRequest"])

# --- CRUD ---

@api_post(router, "", RepairRequestResponseSchema1, summary="Создать заявку на ремонт")
async def create_repair_request(
    repair_request: RepairRequestCreateSchema = Body(...),
    repair_request_service: AbsRepairRequestService = Depends(get_repair_request_service),
):
    try:
        result = await repair_request_service.create_repair_request(pydantic_to_dto(RepairRequestDTO, repair_request))
        if not result:
            raise_404(data={"errors": "RepairRequest not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", RepairRequestResponseSchema2, summary="Получить заявку на ремонт")
async def get_repair_request(
    repair_request: RepairRequestGetSchema = Query(...),
    repair_request_service: AbsRepairRequestService = Depends(get_repair_request_service),
):
    try:
        result = await repair_request_service.get_repair_request(pydantic_to_dto(RepairRequestDTO, repair_request))
        if not result:
            raise_404(data={"errors": "RepairRequest not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", RepairRequestResponseSchema3, summary="Обновить заявку на ремонт")
async def update_repair_request(
    repair_request: RepairRequestUpdateSchema = Body(...),
    repair_request_service: AbsRepairRequestService = Depends(get_repair_request_service),
):
    try:
        result = await repair_request_service.update_repair_request(pydantic_to_dto(RepairRequestDTO, repair_request))
        if not result:
            raise_404(data={"errors": "RepairRequest not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", RepairRequestResponseSchema4, summary="Удалить заявку на ремонт")
async def delete_repair_request(
    repair_request: RepairRequestDeleteSchema = Body(...),
    repair_request_service: AbsRepairRequestService = Depends(get_repair_request_service),
):
    try:
        result = await repair_request_service.delete_repair_request(pydantic_to_dto(RepairRequestDTO, repair_request))
        if not result:
            raise_404(data={"errors": "RepairRequest not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

# --- Дополнительные endpoint-ы ---

@api_get(router, "/list", RepairRequestListSchema, summary="Список всех заявок на ремонт")
async def list_repair_requests(
    status: str = Query(None, description="Статус"),
    priority: str = Query(None, description="Приоритет"),
    skip: int = Query(0), limit: int = Query(10),
):
    # Заглушка
    from datetime import datetime
    return [
        RepairRequestResponseSchema1(
            id=str(i),
            vehicle_id=f"v{i%5}",
            description=f"Неисправность {i}",
            status=status or "open",
            priority=priority or "normal",
            requested_by="u1",
            approved_by="u2",
            created_at=datetime.now(),
            closed_at=datetime.now()
        ) for i in range(skip, skip + limit)
    ]

@api_put(router, "/batch/status", RepairRequestBatchStatusResponseSchema, summary="Массовое изменение статусов заявок")
async def batch_update_repair_status(
    batch: RepairRequestBatchStatusSchema = Body(...),
):
    from datetime import datetime
    # Заглушка: возвращаем заявки с новым статусом
    return [
        RepairRequestResponseSchema1(
            id=req_id,
            vehicle_id=f"v{idx}",
            description=f"Bulk update for {req_id}",
            status=batch.status,
            priority="normal",
            requested_by="u1",
            approved_by="u2",
            created_at=datetime.now(),
            closed_at=datetime.now()
        ) for idx, req_id in enumerate(batch.ids)
    ]

@api_get(router, "/{repair_request_id}/history", RepairRequestHistoryListSchema, summary="История изменений статуса заявки")
async def repair_request_history(
    repair_request_id: str,
):
    from datetime import datetime, timedelta
    now = datetime.now()
    return [
        {"timestamp": now - timedelta(days=3), "status": "created", "comment": "Заявка создана"},
        {"timestamp": now - timedelta(days=2), "status": "in_work", "comment": "В работе"},
        {"timestamp": now, "status": "closed", "comment": "Заявка закрыта"}
    ]

@api_get(router, "/stats", RepairRequestStatsSchema, summary="Статистика по заявкам на ремонт")
async def repair_request_stats():
    return RepairRequestStatsSchema(
        total=32, open=5, closed=27, urgent=2, avg_close_time_hours=36.5
    )
