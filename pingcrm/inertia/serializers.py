from django.contrib import messages
from rest_framework import serializers, fields


class InertiaResult(object):
    def __init__(self, component, url, data, version=None, only=None):
        self.component = component
        self.version = version
        self.url = url
        self.data = data
        self.only = only or []


class InertiaSerializer(serializers.Serializer):
    component = serializers.CharField()
    props = serializers.SerializerMethodField()
    version = serializers.CharField()
    url = serializers.URLField(source='path')

    def get_props(self, obj):
        if hasattr(settings, 'INERTIA_SHARED_SERIALIZER_CLASS'):
            serializer_class = settings.INERTIA_SHARED_SERIALIZER_CLASS
        else:
            serializer_class = SharedSerializer
        serializer = serializer_class(obj, context=self.context)
        return serializer.data


class SharedSerializer(serializers.Serializer):
    def __init__(self, instance, *args, **kwargs):
        # exclude keys already included in data
        exclude = instance.data.keys()

        # exclude fields not included in only (if there is an only)
        if instance.only:
            exclude = [field for field in self.fields if field not in instance.only]
            for field in exclude:
                if field in self.fields:
                    self.fields.pop(field)

        super(SharedSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        # merge the shared data with the component data
        data = super(SharedSerializer, self).to_representation(instance).copy()
        data.update(instance.data)
        return data


class SharedField(fields.Field):
    """
    Shared fields by default are Read-only and require a context
    """
    requires_context = True

    def __init__(self, **kwargs):
        kwargs['read_only'] = True
        super().__init__(**kwargs)


class FlashField(SharedField):
    def to_representation(self, value):
        flash = {}
        try:
            storage = messages.get_messages(self.context["request"])
            for message in storage:
                flash[message.level_tag] = message.message
        except:
            pass
        return flash


class SessionErrorsField(SharedField):
    def to_representation(self, value):
        try:
            return self.context["request"].session["errors"]
        except:
            pass
        return {}
