from collections.abc import Awaitable
from functools import wraps
from typing import Any, Callable, Type, TypeVar

from fastapi import APIRouter

from v1.src.api.rest.exceptions.schemas import (
    BaseResponse,
    ErrorCode,
    ErrorResponse,
    SuccessResponse,
)

# ---------- Конфигурация ошибок ----------

def make_error_response(
    code: int,
    description: str,
    error_code: ErrorCode,
    details: str,
    data: dict | None = None,
) -> dict:
    return {
        "model": ErrorResponse,
        "description": description,
        "content": {
            "application/json": {
                "example": {
                    "status": "error",
                    "error_code": error_code,
                    "data": data,
                    "details": details,
                }
            }
        }
    }


DEFAULT_ERROR_RESPONSES = {
    400: make_error_response(
        code=400,
        description="Bad Request",
        error_code=ErrorCode.bad_request,
        details="Некорректный запрос",
        data={"errors": {}}
    ),
    401: make_error_response(
        code=401,
        description="Unauthorized",
        error_code=ErrorCode.unauthorized,
        details="Неавторизованный доступ",
        data={"errors": {}}
    ),
    403: make_error_response(
        code=403,
        description="Forbidden",
        error_code=ErrorCode.forbidden,
        details="Доступ запрещён",
        data={"errors": {}}
    ),
    404: make_error_response(
        code=404,
        description="Not Found",
        error_code=ErrorCode.not_found,
        details="Ресурс не найден",
        data={"errors": {}}
    ),
    409: make_error_response(
        code=409,
        description="Conflict",
        error_code=ErrorCode.conflict,
        details="Конфликт данных",
        data={"errors": {}}
    ),
    413: make_error_response(
        code=413,
        description="Payload Too Large",
        error_code=ErrorCode.payload_too_large,
        details="Слишком большой запрос",
        data={"errors": {}}
    ),
    422: make_error_response(
        code=422,
        description="Validation Error",
        error_code=ErrorCode.validation_error,
        details="Ошибка валидации запроса",
        data={"errors": {"field": "is required"}}
    ),
    429: make_error_response(
        code=429,
        description="Rate Limit",
        error_code=ErrorCode.rate_limit,
        details="Слишком много запросов",
        data={"errors": {}}
    ),
    500: make_error_response(
        code=500,
        description="Internal Error",
        error_code=ErrorCode.internal_error,
        details="Внутренняя ошибка",
        data={"errors": {}}
    ),
    501: make_error_response(
        code=501,
        description="Not Implemented",
        error_code=ErrorCode.not_implemented,
        details="Метод не реализован",
        data={"errors": {}}
    ),
    502: make_error_response(
        code=502,
        description="Bad Gateway",
        error_code=ErrorCode.bad_gateway,
        details="Ошибка шлюза",
        data={"errors": {}}
    ),
    503: make_error_response(
        code=503,
        description="Service Unavailable",
        error_code=ErrorCode.service_unavailable,
        details="Сервис временно недоступен",
        data={"errors": {}}
    ),
    504: make_error_response(
        code=504,
        description="Gateway Timeout",
        error_code=ErrorCode.timeout,
        details="Таймаут шлюза",
        data={"errors": {}}
    ),
}


# ---------- Обёртка успеха ----------

T = TypeVar("T")


def wrap_success_response(details: str = "") -> Callable[[Callable[..., Awaitable[T]]], Callable[..., Awaitable[SuccessResponse[T]]]]:
    def decorator(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[SuccessResponse[T]]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> SuccessResponse[T]:
            result = await func(*args, **kwargs)
            return SuccessResponse(status="success", data=result, details=details)
        return wrapper
    return decorator


# ---------- Универсальный API-декоратор ----------

def _api_method(
    router_method: Callable,
    router: APIRouter,
    path: str,
    payload_type: Type[Any],
    details: str = "",
    **kwargs
):
    def decorator(func: Callable):
        route_decorator = router_method(
            path,
            response_model=BaseResponse(payload_type),
            responses=DEFAULT_ERROR_RESPONSES,
            **kwargs
        )
        wrapped = wrap_success_response(details=details)(func)
        return route_decorator(wrapped)
    return decorator


# ---------- Конкретные методы ----------

def api_get(router: APIRouter, path: str, payload_type: Type[Any], *, details: str = "", **kwargs):
    return _api_method(router.get, router, path, payload_type, details=details, **kwargs)


def api_post(router: APIRouter, path: str, payload_type: Type[Any], *, details: str = "", **kwargs):
    return _api_method(router.post, router, path, payload_type, details=details, **kwargs)


def api_put(router: APIRouter, path: str, payload_type: Type[Any], *, details: str = "", **kwargs):
    return _api_method(router.put, router, path, payload_type, details=details, **kwargs)


def api_delete(router: APIRouter, path: str, payload_type: Type[Any], *, details: str = "", **kwargs):
    return _api_method(router.delete, router, path, payload_type, details=details, **kwargs)
