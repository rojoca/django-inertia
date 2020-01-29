import logging
from rest_framework import status, views
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied, NotAuthenticated


LOGIN_REDIRECT="/login" # getattr(settings, 'INERTIA_LOGIN_REDIRECT', '/login')
logger = logging.getLogger('django')


def inertia_exception_handler(exc, context):
    override_status = None
    override_headers = {}
    if isinstance(exc, ValidationError):
        logger.info("Got a validation error")
        context['request'].session['errors'] = exc.detail
        override_headers["Location"] = context['request'].path
        override_status = status.HTTP_302_FOUND

    if isinstance(exc, PermissionDenied) or isinstance(exc, NotAuthenticated):
        override_status = status.HTTP_302_FOUND
        override_headers["Location"] = LOGIN_REDIRECT

    # use rest framework exception handler
    response = views.exception_handler(exc, context)

    if override_status:
        response.status_code = override_status

    if response.status_code == 409:
        response['X-Inertia-Location'] = context['request'].path

    for header in override_headers:
        response[header] = override_headers[header]

    logger.info(override_headers)

    return response
