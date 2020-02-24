from rest_framework import serializers
from inertia.serializers import DefaultSharedSerializer

from .models import User, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.CharField(source="photo_path", read_only=True)
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ('email', 'photo', 'role', 'first_name', 'last_name', 'account')


class AuthSerializer(serializers.Serializer):
    user = UserSerializer()


class InertiaSharedSerializer(DefaultSharedSerializer):
    auth = AuthSerializer("*")

    class Meta:
        fields = ('flash', 'errors', 'auth')
