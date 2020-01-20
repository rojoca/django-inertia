from rest_framework import status, views
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied, NotAuthenticated


def inertia_exception_handler(exc, context):
    override_status = None
    overrid_headers = {}
    if isinstance(exc, ValidationError):
        override_status = status.HTTP_422_UNPROCESSABLE_ENTITY

    if isinstance(exc, PermissionDenied) or isinstance(exc, NotAuthenticated):
        override_status = status.HTTP_302_FOUND
        overrid_headers["Location"] = LOGIN_REDIRECT

    # use rest framework exception handler
    response = views.exception_handler(exc, context)

    if override_status:
        response.status = override_status

    if response.status == 409:
        response.headers['X-Inertia-Location'] = request.path

    return response
