import logging
from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponseRedirect
from rest_framework import serializers, viewsets, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from inertia.views import inertia
from .serializers import UserSerializer

logger = logging.getLogger('django')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


@inertia("Auth/Login")
class Login(views.APIView):
    def get(self, request, format=None):
        return Response(data={})

    def post(self, request, format=None):
        s = LoginSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        user = authenticate(request, username=s.validated_data['email'], password=s.validated_data['password'])
        if not user:
            raise serializers.ValidationError({"email": ["These credentials do not match our records."]})

        login(request, user)

        return HttpResponseRedirect(redirect_to="/")


class LoggedInView(views.APIView):
    permission_classes = [IsAuthenticated]


@inertia("Dashboard/Index")
class Dashboard(LoggedInView):
    pass


@inertia("User/Index")
class User(LoggedInView):
    pass


@inertia("User/Edit")
class UserEdit(LoggedInView):
    pass


@inertia("User/Create")
class UserCreate(LoggedInView):
    pass

