from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.refueling_log.dependencies import get_refueling_log_service, AbsRefuelingLogService
from v1.src.app.dto.refueling_log import RefuelingLogDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.refueling_log.schemas import (
    RefuelingLogCreateSchema, RefuelingLogGetSchema, RefuelingLogUpdateSchema, RefuelingLogDeleteSchema,
    RefuelingLogResponseSchema1, RefuelingLogResponseSchema2, RefuelingLogResponseSchema3, RefuelingLogResponseSchema4
)

router = APIRouter(prefix="/refueling_log", tags=["RefuelingLog"])

@api_post(router, "", RefuelingLogResponseSchema1, summary="Создать запись о заправке")
async def create_refueling_log(
    refueling_log: RefuelingLogCreateSchema = Body(...),
    refueling_log_service: AbsRefuelingLogService = Depends(get_refueling_log_service),
):
    try:
        result = await refueling_log_service.create_refueling_log(pydantic_to_dto(RefuelingLogDTO, refueling_log))
        if not result:
            raise_404(data={"errors": "RefuelingLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", RefuelingLogResponseSchema2, summary="Получить запись о заправке")
async def get_refueling_log(
    refueling_log: RefuelingLogGetSchema = Query(...),
    refueling_log_service: AbsRefuelingLogService = Depends(get_refueling_log_service),
):
    try:
        result = await refueling_log_service.get_refueling_log(pydantic_to_dto(RefuelingLogDTO, refueling_log))
        if not result:
            raise_404(data={"errors": "RefuelingLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", RefuelingLogResponseSchema3, summary="Обновить запись о заправке")
async def update_refueling_log(
    refueling_log: RefuelingLogUpdateSchema = Body(...),
    refueling_log_service: AbsRefuelingLogService = Depends(get_refueling_log_service),
):
    try:
        result = await refueling_log_service.update_refueling_log(pydantic_to_dto(RefuelingLogDTO, refueling_log))
        if not result:
            raise_404(data={"errors": "RefuelingLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", RefuelingLogResponseSchema4, summary="Удалить запись о заправке")
async def delete_refueling_log(
    refueling_log: RefuelingLogDeleteSchema = Body(...),
    refueling_log_service: AbsRefuelingLogService = Depends(get_refueling_log_service),
):
    try:
        result = await refueling_log_service.delete_refueling_log(pydantic_to_dto(RefuelingLogDTO, refueling_log))
        if not result:
            raise_404(data={"errors": "RefuelingLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
