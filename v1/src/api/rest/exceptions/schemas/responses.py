# v1/src/api/rest/exceptions/schemas/responses.py
from typing import Generic, Optional, Type, TypeVar, Union

from pydantic import BaseModel, Field

from v1.src.api.rest.exceptions.schemas.errors import ErrorCode

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    status: str = Field(default="success", description="Request status (always success)")
    data: Optional[T] = Field(default=None, description="Returned data")
    details: Optional[str] = Field(default="", description="Additional details about the response")


class ErrorResponse(BaseModel):
    status: str = Field(default="error", description="Always error")
    error_code: ErrorCode = Field(..., description="Machine-readable error code")
    data: Optional[dict] = Field(default=None, description="Optional error payload")
    details: str = Field(..., description="Human-readable description")


def BaseResponse(of_type: Type) -> Type[Union[SuccessResponse, ErrorResponse]]:
    return Union[SuccessResponse[of_type], ErrorResponse]
