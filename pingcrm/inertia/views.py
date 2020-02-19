import logging
from functools import wraps
from rest_framework import status, response, views, viewsets, generics, exceptions

from .negotiation import InertiaNegotiation, InertiaHTMLRenderer, InertiaJSONRenderer
from .exceptions import Conflict

logger = logging.getLogger('django')

TEMPLATE_NAME="index.html" # getattr(settings, 'INERTIA_TEMPLATE_NAME', 'index.html')


def get_asset_version():
    pass


class InertiaHeaders(object):
    version = None
    component = None
    only = None

    def include(self, name):
        return self.only and name in self.only


class InertiaResponse(response.Response):

    def __init__(self, wrapped_response, component):
        self.wrapped_response = wrapped_response
        self.component = component

    def __getattribute__(self, name):
        if name == "component":
            return self.component

        return self.wrapped_response.__getattribute__(name)


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER



def inertia(APIViewClass, component_path, template_name=None, **component_map):
    class WrappedInertiaView(object):
        content_negotiation_class = InertiaNegotiation

        def __init__(self, *args, **kwargs):
            self._api_class_instance = APIViewClass(*args, **kwargs)

        def __getattribute__(self, name):
            try:
                attr = super(WrappedInertiaView, self).__getattribute__(name)
            except AttributeError:
                pass
            else:
                return attr

            attr = self._api_class_instance.__getattribute__(name)

            # if attr name in list of components, decorate the method
            # with the component decorator
            if name in component_map:
                return component(attr, component_map[name])
            return attr

        @property
        def default_response_headers(self):
            headers = self._api_class_instance.default_response_headers
            headers["X-Inertia"] = True
            return headers

        def get_renderer_context(self):
            context = self._api_class_instance.get_renderer_context()
            context["template_name"] = template_name
            context["component"] = component_path
            return context

        def initialize_inertia(self, request):
            """
            Get the inertia variables from the request headers if they exist
            """
            is_inertia = request.META.get('HTTP_X_INERTIA', False)

            if is_inertia:
                self.inertia = InertiaHeaders()
                if request.method == 'get':
                    # Check version is current
                    self.inertia.version = request.META.get('HTTP_X_INERTIA_VERSION', None)
                    if self.inertia.version != get_asset_version():
                        raise Conflict()

                # set partial details if they exist
                self.inertia.component = request.META.get('HTTP_X_INERTIA_PARTIAL_COMPONENT', None)
                only = request.META.get('HTTP_X_INERTIA_PARTIAL_DATA', None)
                if only:
                    self.inertia.only = only.split(',')

        def initialize_request(self, request, *args, **kwargs):
            request = self._api_class_instance.initialize_request(request, *args, **kwargs)

            self.initialize_inertia(request)
            if not hasattr(request, 'inertia'):
                Request.inertia = property(lambda self: self.inertia)

            return request


    return WrappedInertiaView


def component(component_path):
    """
    Sets the component for a method within a class based view.

    Can only be applied to methods inside APIView classes
    that return Response objects:

    ````
        class MyViewSet(ModelViewSet):
           # ...
           @component("My/Component")
           def retrieve(self, request, *args, **kwargs):
                # ...
                return Response(serializer.data)
    ````
    """
    def method_decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            response = method(*args, **kwargs)

            if isinstance(response, response.Response):
                # monkey patch response
                response.component = component_path
            return response
        return wrapper
    return method_decorator

