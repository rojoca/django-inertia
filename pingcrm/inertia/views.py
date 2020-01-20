from rest_framework import status, response, views


TEMPLATE_NAME="index.html" # getattr(settings, 'INERTIA_TEMPLATE_NAME', 'index.html')
LOGIN_REDIRECT="/login" # getattr(settings, 'INERTIA_LOGIN_REDIRECT', '/login')


def get_asset_version():
    pass


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER


class Response(response.Response):
    template_name = TEMPLATE_NAME


class InertiaViewMixin(object):
    content_negotiation_class = 'inertia.negotiation.InertiaNegotiation'


class InertiaView(InertiaViewMixin, views.APIView):
    def get(self, request, format=None):
        return Response(data={})
