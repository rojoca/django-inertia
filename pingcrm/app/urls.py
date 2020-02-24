from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)


app_name = "app"
urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('login', views.Login.as_view(), name="login"),
    url(r'users/', include((router.urls, 'app_name'), namespace='instance_name')),
]

urlpatterns += router.urls
