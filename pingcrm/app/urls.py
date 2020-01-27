from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('login', views.Login.as_view(), name="login")
]
