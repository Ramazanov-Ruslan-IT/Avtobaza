# v1/src/api/rest/exceptions/raisers.py
from v1.src.api.rest.exceptions.app_exceptions import AppException
from v1.src.api.rest.exceptions.schemas.errors import ErrorCode


def raise_401(detail="Unauthorized", data=None):
    raise AppException(401, ErrorCode.unauthorized, detail, data)


def raise_403(detail="Forbidden", data=None):
    raise AppException(403, ErrorCode.forbidden, detail, data)


def raise_404(detail="Not Found", data=None):
    raise AppException(404, ErrorCode.not_found, detail, data)


def raise_422(detail="Validation Error", data=None):
    raise AppException(422, ErrorCode.validation_error, detail, data)


def raise_409(detail="Conflict", data=None):
    raise AppException(409, ErrorCode.conflict, detail, data)


def raise_409_already_exists(detail="Already exists", data=None):
    raise AppException(409, ErrorCode.already_exists, detail, data)


def raise_400(detail="Bad Request", data=None):
    raise AppException(400, ErrorCode.bad_request, detail, data)


def raise_413(detail="Payload Too Large", data=None):
    raise AppException(413, ErrorCode.payload_too_large, detail, data)


def raise_429(detail="Too Many Requests", data=None):
    raise AppException(429, ErrorCode.rate_limit, detail, data)


def raise_500(detail="Internal Server Error", data=None):
    raise AppException(500, ErrorCode.internal_error, detail, data)


def raise_503(detail="Service Unavailable", data=None):
    raise AppException(503, ErrorCode.service_unavailable, detail, data)


def raise_504(detail="Gateway Timeout", data=None):
    raise AppException(504, ErrorCode.timeout, detail, data)


def raise_501(detail="Not Implemented", data=None):
    raise AppException(501, ErrorCode.not_implemented, detail, data)


def raise_502(detail="Bad Gateway", data=None):
    raise AppException(502, ErrorCode.bad_gateway, detail, data)


def raise_499_dependency_failed(detail="Dependency failed", data=None):
    raise AppException(499, ErrorCode.dependency_failed, detail, data)


def raise_498_token_expired(detail="Token expired", data=None):
    raise AppException(498, ErrorCode.token_expired, detail, data)


def raise_403_permission_denied(detail="Permission denied", data=None):
    raise AppException(403, ErrorCode.permission_denied, detail, data)


def raise_403_user_inactive(detail="User inactive", data=None):
    raise AppException(403, ErrorCode.user_inactive, detail, data)


def raise_401_invalid_credentials(detail="Invalid credentials", data=None):
    raise AppException(401, ErrorCode.invalid_credentials, detail, data)


def raise_503_maintenance(detail="Service in maintenance mode", data=None):
    raise AppException(503, ErrorCode.maintenance, detail, data)
