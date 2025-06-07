from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.access_log.dependencies import get_access_log_service, AbsAccessLogService
from v1.src.app.dto.access_log import AccessLogDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.access_log.schemas import (
    AccessLogCreateSchema, AccessLogGetSchema, AccessLogUpdateSchema, AccessLogDeleteSchema,
    AccessLogResponseSchema1, AccessLogResponseSchema2, AccessLogResponseSchema3, AccessLogResponseSchema4
)

router = APIRouter(prefix="/access_log", tags=["AccessLog"])


@api_post(router, "", AccessLogResponseSchema1, summary="Создать access_log")
async def create_access_log(
    access_log: AccessLogCreateSchema = Body(...),
    access_log_service: AbsAccessLogService = Depends(get_access_log_service),
):
    try:
        result = await access_log_service.create_access_log(pydantic_to_dto(AccessLogDTO, access_log))
        if not result:
            raise_404(data={"errors": "AccessLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_get(router, "", AccessLogResponseSchema2, summary="Получить access_log")
async def get_access_log(
    access_log: AccessLogGetSchema = Query(...),
    access_log_service: AbsAccessLogService = Depends(get_access_log_service),
):
    try:
        result = await access_log_service.get_access_log(pydantic_to_dto(AccessLogDTO, access_log))
        if not result:
            raise_404(data={"errors": "AccessLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_put(router, "", AccessLogResponseSchema3, summary="Обновить access_log")
async def update_access_log(
    access_log: AccessLogUpdateSchema = Body(...),
    access_log_service: AbsAccessLogService = Depends(get_access_log_service),
):
    try:
        result = await access_log_service.update_access_log(pydantic_to_dto(AccessLogDTO, access_log))
        if not result:
            raise_404(data={"errors": "AccessLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_delete(router, "", AccessLogResponseSchema4, summary="Удалить access_log")
async def delete_access_log(
    access_log: AccessLogDeleteSchema = Body(...),
    access_log_service: AbsAccessLogService = Depends(get_access_log_service),
):
    try:
        result = await access_log_service.delete_access_log(pydantic_to_dto(AccessLogDTO, access_log))
        if not result:
            raise_404(data={"errors": "AccessLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
