from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.maintenance_log.dependencies import get_maintenance_log_service, AbsMaintenanceLogService
from v1.src.app.dto.maintenance_log import MaintenanceLogDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.maintenance_log.schemas import (
    MaintenanceLogCreateSchema, MaintenanceLogGetSchema, MaintenanceLogUpdateSchema, MaintenanceLogDeleteSchema,
    MaintenanceLogResponseSchema1, MaintenanceLogResponseSchema2, MaintenanceLogResponseSchema3, MaintenanceLogResponseSchema4
)

router = APIRouter(prefix="/maintenance_log", tags=["MaintenanceLog"])

@api_post(router, "", MaintenanceLogResponseSchema1, summary="Создать запись о ТО")
async def create_maintenance_log(
    maintenance_log: MaintenanceLogCreateSchema = Body(...),
    maintenance_log_service: AbsMaintenanceLogService = Depends(get_maintenance_log_service),
):
    try:
        result = await maintenance_log_service.create_maintenance_log(pydantic_to_dto(MaintenanceLogDTO, maintenance_log))
        if not result:
            raise_404(data={"errors": "MaintenanceLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_get(router, "", MaintenanceLogResponseSchema2, summary="Получить запись о ТО")
async def get_maintenance_log(
    maintenance_log: MaintenanceLogGetSchema = Query(...),
    maintenance_log_service: AbsMaintenanceLogService = Depends(get_maintenance_log_service),
):
    try:
        result = await maintenance_log_service.get_maintenance_log(pydantic_to_dto(MaintenanceLogDTO, maintenance_log))
        if not result:
            raise_404(data={"errors": "MaintenanceLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_put(router, "", MaintenanceLogResponseSchema3, summary="Обновить запись о ТО")
async def update_maintenance_log(
    maintenance_log: MaintenanceLogUpdateSchema = Body(...),
    maintenance_log_service: AbsMaintenanceLogService = Depends(get_maintenance_log_service),
):
    try:
        result = await maintenance_log_service.update_maintenance_log(pydantic_to_dto(MaintenanceLogDTO, maintenance_log))
        if not result:
            raise_404(data={"errors": "MaintenanceLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})

@api_delete(router, "", MaintenanceLogResponseSchema4, summary="Удалить запись о ТО")
async def delete_maintenance_log(
    maintenance_log: MaintenanceLogDeleteSchema = Body(...),
    maintenance_log_service: AbsMaintenanceLogService = Depends(get_maintenance_log_service),
):
    try:
        result = await maintenance_log_service.delete_maintenance_log(pydantic_to_dto(MaintenanceLogDTO, maintenance_log))
        if not result:
            raise_404(data={"errors": "MaintenanceLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
