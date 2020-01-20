from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponseRedirect
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .inertia import InertiaView, Response


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class Login(InertiaView):
    def post(self, request, format=None):
        s = LoginSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        user = authenticate(s.validated_data['email'], s.validated_data['password'])
        if not user:
            raise serializers.ValidationError("These credentials do not match our records.")

        login(request, user)

        return HttpResponseRedirect(redirect_to="/")


class Dashboard(InertiaView):
    permission_classes = [IsAuthenticated]


