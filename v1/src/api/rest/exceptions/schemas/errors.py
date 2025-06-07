# v1/src/api/rest/exceptions/schemas/errors.py
from enum import Enum


class ErrorCode(str, Enum):
    unauthorized = "unauthorized"
    forbidden = "forbidden"
    not_found = "not_found"
    validation_error = "validation_error"
    http_exception = "http_exception"
    db_error = "db_error"
    internal_error = "internal_error"
    service_unavailable = "service_unavailable"
    bad_gateway = "bad_gateway"
    timeout = "timeout"
    conflict = "conflict"
    already_exists = "already_exists"
    not_implemented = "not_implemented"
    rate_limit = "rate_limit"
    bad_request = "bad_request"
    payload_too_large = "payload_too_large"
    dependency_failed = "dependency_failed"
    token_expired = "token_expired"
    permission_denied = "permission_denied"
    user_inactive = "user_inactive"
    invalid_credentials = "invalid_credentials"
    maintenance = "maintenance"
