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
    inertia_component = None

    def __init__(self, *args, **kwargs):
        self.inertia_component = kwargs.pop('inertia_component')
        if 'template_name' not in kwargs:
            kwargs['template_name'] = TEMPLATE_NAME
        super(Response, self).__init__(*args, **kwargs)


class InertiaViewMixin(object):
    content_negotiation_class = InertiaNegotiation


class InertiaView(InertiaViewMixin, views.APIView):
    inertia_component = 'App'

    def finalize_response(self, request, response, *args, **kwargs):
        response = super(InertiaView, self).finalize_response(request, response, *args, **kwargs)

        if isinstance(response, Response) and not response.inertia_component:
            response.inertia_component = self.inertia_component

        logger.info("FINALIE")
        logger.info(response)
        return response

    def get(self, request, format=None):
        return Response(data={})
