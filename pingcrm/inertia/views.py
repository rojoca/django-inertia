import logging
from rest_framework import status, response, views
from .negotiation import InertiaNegotiation

logger = logging.getLogger('django')

TEMPLATE_NAME="index.html" # getattr(settings, 'INERTIA_TEMPLATE_NAME', 'index.html')


def get_asset_version():
    pass


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER


class Response(response.Response):
    template_name = TEMPLATE_NAME
    inertia_component = 'App'

    def __init__(self, *args, **kwargs):
        self.inertia_component = kwargs.pop('inertia_component')
        super(Response, self).__init__(*args, **kwargs)


class InertiaViewMixin(object):
    content_negotiation_class = InertiaNegotiation


class InertiaView(InertiaViewMixin, views.APIView):

    def finalize_response(self, request, response, *args, **kwargs):
        response = super(InertiaView, self).finalize_response(request, response, *args, **kwargs)
        logger.info(response.renderer_context)
        return response

    def response(self, data={}, status=200, headers={}, template_name=None, content_type=None):
        return Response(
            data=data,
            status=status,
            headers=headers,
            template_name=template_name,
            content_type=content_type,
            context={
                'request': request
            }
        )

    def get(self, request, format=None):
        return Response(data={})
