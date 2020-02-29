import logging
from rest_framework import status, views
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied, NotAuthenticated


LOGIN_REDIRECT="/login" # getattr(settings, 'INERTIA_LOGIN_REDIRECT', '/login')


class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Asset version conflict.'
    default_code = 'conflict'

    def __init__(self, detail=None, code=None, available_renderers=None):
        self.available_renderers = available_renderers
        super().__init__(detail, code)


def inertia_exception_handler(exc, context):
    override_status = None
    override_headers = {}

    request = context['request']
    is_inertia = hasattr(request, 'inertia')

    if is_inertia and isinstance(exc, ValidationError):
        context['request'].session['errors'] = exc.detail
        override_headers["Location"] = context['request'].path
        override_status = status.HTTP_302_FOUND

    if is_inertia and (isinstance(exc, PermissionDenied) or isinstance(exc, NotAuthenticated)):
        override_status = status.HTTP_302_FOUND
        override_headers["Location"] = LOGIN_REDIRECT

    # use rest framework exception handler
    response = views.exception_handler(exc, context)

    if override_status:
        response.status_code = override_status

    if is_inertia and response.status_code == 409:
        response['X-Inertia-Location'] = context['request'].path

    for header in override_headers:
        response[header] = override_headers[header]

    return response
