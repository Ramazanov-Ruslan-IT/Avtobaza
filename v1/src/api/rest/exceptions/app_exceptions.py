# v1/src/api/rest/exceptions/app_exceptions.py
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from v1.src.api.rest.exceptions.schemas.errors import ErrorCode
from v1.src.api.rest.exceptions.schemas.responses import ErrorResponse


class AppException(HTTPException):
    def __init__(self, status_code: int, error_code: ErrorCode, detail: str, data: dict | None = None):
        self.error_code = error_code
        self.data = data if data is not None else {"errors": {}}
        super().__init__(status_code=status_code, detail=detail)


async def app_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                status="error",
                error_code=exc.error_code,
                data=exc.data,
                details=exc.detail
            ).model_dump()
        )
    raise exc
