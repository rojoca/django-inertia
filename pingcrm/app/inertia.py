from rest_framework import status, response, views
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied, NotAuthenticated


TEMPLATE_NAME="index.html" # getattr(settings, 'INERTIA_TEMPLATE_NAME', 'index.html')
LOGIN_REDIRECT="/login" # getattr(settings, 'INERTIA_LOGIN_REDIRECT', '/login')


def get_asset_version():
    pass


class InertiaRedirect(response.Response):
    status_code = status.HTTP_303_SEE_OTHER


class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Asset version conflict.'
    default_code = 'conflict'

    def __init__(self, detail=None, code=None, available_renderers=None):
        self.available_renderers = available_renderers
        super().__init__(detail, code)


class InertiaRendererMixin(object):
    partial_component = None
    partial_only = None

    def get_only(self, response_component):
        # Only return only if the partial component matches the response component
        if self.partial_only and response_component == self.partial_component:
            return only
        return None

    def apply_shared(self, data, only=None):
        # TODO: apply shared data to data
        # - only add if not in only
        # - only add if prop does not already exist in data

        if only:
            # filter props by only (X-Inertial-Partial-Data)
            return {k: data[k] for k in only}

        return data

    def apply(data, renderer_context):
        request = renderer_context['request']
        response = renderer_context['response']

        # if the response has an inertia_component
        # return inertia data
        if response.inertia_component:
            only = request.inertial_partial.get_only(response.inertia_component)
            return {
                "component": response.inertia_component,
                "props": self.apply_shared(data, only=only),
                "url": request.path,
                "version": get_asset_version()
            }

        # return regular data
        return data

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = self.apply(data, renderer_context)
        return super(InertiaRendererMixin, self).render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class InertiaHTMLRenderer(InertiaRendererMixin, TemplateHTMLRenderer):
    pass


class InertiaJSONRenderer(InertiaRendererMixin, TemplateHTMLRenderer):
    pass


class InertiaNegotiation(DefaultContentNegotiation):

    def select_renderer(self, request, renderers, format_suffix=None):
        # check for inertia headers:
        is_inertia = request.META.get('HTTP_X_INERTIA', False)

        if is_inertia:
            if request.method == 'get':
                version = request.META.get('HTTP_X_INERTIA_VERSION', None)
                if version != get_asset_version():
                    raise Conflict()

            renderer = InertiaJSONRenderer()
            renderer.partial_component = request.META.get('HTTP_X_INERTIA_PARTIAL_COMPONENT', None)
            renderer.partial_only = request.META.get('HTTP_X_INERTIA_PARTIAL_DATA', None)
            media_type = "application/json"
        else:
            renderer, media_type = super(InertiaNegotiation, self).select_renderer(request, renderers, format_suffix=format_suffix)

        return (renderer, media_type)


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


class Response(response.Response):
    template_name = TEMPLATE_NAME


class InertiaViewMixin(object):
    content_negotiation_class = InertiaNegotiation


class InertiaView(InertiaViewMixin, views.APIView):
    def get(self, request, format=None):
        return Response(data={})


