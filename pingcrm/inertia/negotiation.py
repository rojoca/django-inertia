import logging
import json
from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.negotiation import DefaultContentNegotiation
from .serializers import InertiaSerializer, InertiaResult

logger = logging.getLogger('django')


def get_asset_version():
    return "test"


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
    shared_serializer_class = settings.INERTIA_SHARED_SERIALIER_CLASS

    def render(self, data, accepted_media_type=None, renderer_context=None):
        only = []
        if self.partial_component == renderer_context["component"]:
            only = self.partial_only

        result = InertiaResult(
            renderer_context["component"],
            renderer_context["request"].path,
            data,
            version=get_asset_version(),
            only=only
        )

        serializer = InertiaSerializer(result, context=renderer_context)
        return super(InertiaRendererMixin, self).render(
            serializer.data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class InertiaHTMLRenderer(InertiaRendererMixin, TemplateHTMLRenderer):

    def get_template_context(self, data, renderer_context):
        # allow data to be injected into template
        return super(InertiaHTMLRenderer, self).get_template_context(data, renderer_context)

    def render(self, data, accepted_media_type=None, renderer_context=None):
        self.template_name = renderer_context.get("template_name") or settings.INERTIA_HTML_TEMPLATE
        return super(self, data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class InertiaJSONRenderer(InertiaRendererMixin, JSONRenderer):
    pass


class InertiaNegotiation(DefaultContentNegotiation):
    html_renderer = InertiaHTMLRenderer
    json_renderer = InertiaJSONRenderer

    def select_renderer(self, request, renderers, format_suffix=None):
        # check for inertia headers:
        is_inertia = request.META.get('HTTP_X_INERTIA', False)

        if is_inertia:
            if request.method == 'get':
                version = request.META.get('HTTP_X_INERTIA_VERSION', None)
                if version != get_asset_version():
                    raise Conflict()

            renderer = self.json_renderer()
            renderer.partial_component = request.META.get('HTTP_X_INERTIA_PARTIAL_COMPONENT', None)
            renderer.partial_only = request.META.get('HTTP_X_INERTIA_PARTIAL_DATA', None)
            media_type = "application/json"
        else:
            renderer, media_type = super(InertiaNegotiation, self).select_renderer(
                request, renderers, format_suffix=format_suffix)
            if media_type == "text/html":
                renderer = self.html_renderer()

        return (renderer, media_type)
