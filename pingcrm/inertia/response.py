from rest_framework import response, status


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER
