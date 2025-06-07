from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.repair_request.dependencies import get_repair_request_service, AbsRepairRequestService
from v1.src.app.dto.repair_request import RepairRequestDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.repair_request.schemas import (
    RepairRequestCreateSchema, RepairRequestGetSchema, RepairRequestUpdateSchema, RepairRequestDeleteSchema,
    RepairRequestResponseSchema1, RepairRequestResponseSchema2, RepairRequestResponseSchema3, RepairRequestResponseSchema4
)

router = APIRouter(prefix="/repair_request", tags=["RepairRequest"])

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
