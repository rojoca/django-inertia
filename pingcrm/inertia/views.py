import logging
from rest_framework import status, response, views, viewsets, generics
from .negotiation import InertiaNegotiation, InertiaHTMLRenderer, InertiaJSONRenderer

logger = logging.getLogger('django')

TEMPLATE_NAME="index.html" # getattr(settings, 'INERTIA_TEMPLATE_NAME', 'index.html')


def get_asset_version():
    pass


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER



def inertia(APIViewClass, component, template_name=None):
    class WrappedInertiaView(object):
        content_negotiation_class = InertiaNegotiation

        def __init__(self, *args, **kwargs):
            self._api_class_instance = APIViewClass(*args, **kwargs)

        def __getattribute__(self, name):
            try:
                attr = super(APIViewClass, self).__getattribute__(name)
            except AttributeError:
                pass
            else:
                return attr

            return self._api_class_instance.__getattribute__(name)

        @property
        def default_response_headers(self):
            headers = self._api_class_instance.default_response_headers
            headers["X-Inertia"] = True
            return headers

        def get_renderer_context(self):
            context = self._api_class_instance.get_renderer_context()
            context["component"] = component
            context["template_name"] = template_name
            return context

    return WrappedInertiaView

