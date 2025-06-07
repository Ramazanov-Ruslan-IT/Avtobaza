from fastapi import Depends, Body, APIRouter, Query

from v1.src.api.rest.api_route_factory import api_get, api_post, api_put, api_delete
from v1.src.api.rest.exceptions.raisers import raise_500, raise_404

from v1.src.api.rest.routers.audit_log.dependencies import get_audit_log_service, AbsAuditLogService
from v1.src.app.dto.audit_log import AuditLogDTO
from v1.src.app.utils.mapper import pydantic_to_dto

from v1.src.api.rest.routers.audit_log.schemas import (
    AuditLogCreateSchema, AuditLogGetSchema, AuditLogUpdateSchema, AuditLogDeleteSchema,
    AuditLogResponseSchema1, AuditLogResponseSchema2, AuditLogResponseSchema3, AuditLogResponseSchema4
)

router = APIRouter(prefix="/audit_log", tags=["AuditLog"])


@api_post(router, "", AuditLogResponseSchema1, summary="Создать audit_log")
async def create_audit_log(
    audit_log: AuditLogCreateSchema = Body(...),
    audit_log_service: AbsAuditLogService = Depends(get_audit_log_service),
):
    try:
        result = await audit_log_service.create_audit_log(pydantic_to_dto(AuditLogDTO, audit_log))
        if not result:
            raise_404(data={"errors": "AuditLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_get(router, "", AuditLogResponseSchema2, summary="Получить audit_log")
async def get_audit_log(
    audit_log: AuditLogGetSchema = Query(...),
    audit_log_service: AbsAuditLogService = Depends(get_audit_log_service),
):
    try:
        result = await audit_log_service.get_audit_log(pydantic_to_dto(AuditLogDTO, audit_log))
        if not result:
            raise_404(data={"errors": "AuditLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_put(router, "", AuditLogResponseSchema3, summary="Обновить audit_log")
async def update_audit_log(
    audit_log: AuditLogUpdateSchema = Body(...),
    audit_log_service: AbsAuditLogService = Depends(get_audit_log_service),
):
    try:
        result = await audit_log_service.update_audit_log(pydantic_to_dto(AuditLogDTO, audit_log))
        if not result:
            raise_404(data={"errors": "AuditLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})


@api_delete(router, "", AuditLogResponseSchema4, summary="Удалить audit_log")
async def delete_audit_log(
    audit_log: AuditLogDeleteSchema = Body(...),
    audit_log_service: AbsAuditLogService = Depends(get_audit_log_service),
):
    try:
        result = await audit_log_service.delete_audit_log(pydantic_to_dto(AuditLogDTO, audit_log))
        if not result:
            raise_404(data={"errors": "AuditLog not found"})
        return result
    except Exception as e:
        raise_500(data={"errors": str(e)})
