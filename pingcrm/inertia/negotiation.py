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


class InertiaRendererMixin(object):
    partial_component = None
    partial_only = None
    shared_serializer_class = settings.INERTIA_SHARED_SERIALIER_CLASS

    def get_inertia_component(self, renderer_context):
        if "response" in renderer_context and renderer_context["response"].component:
            return renderer_context["response"].component

        return renderer_context["component"]

    def render(self, data, accepted_media_type=None, renderer_context=None):
        component = self.get_inertia_component(renderer_context)
        only = []
        if self.partial_component == component:
            only = self.partial_only

        result = InertiaResult(
            component,
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
        if request.inertia:
            renderer = self.json_renderer()
            renderer.partial_component = request.inertia.component
            renderer.partial_only = request.inertia.only
            media_type = "application/json"
        else:
            renderer, media_type = super(InertiaNegotiation, self).select_renderer(
                request, renderers, format_suffix=format_suffix)
            if media_type == "text/html":
                renderer = self.html_renderer()

        return (renderer, media_type)
