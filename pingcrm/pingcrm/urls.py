"""pingcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from js_urls.views import JsUrlsView

from app import views

app_name = "pingcrm"
urlpatterns = [
    path(r'^js-urls/$', JsUrlsView.as_view(), name='js_urls'),
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('login', views.Login.as_view(), name="login")
]

handler500 = 'django.views.defaults.server_error'
