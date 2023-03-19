"""Omnilegents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Omni import views as OmniViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OmniViews.login, name="login"),
    path('home/', OmniViews.home, name="home"),
    path("libros/", OmniViews.libros, name="libros"), #Para acceder a esta es el mismo enlace con /libros
    path("mislibros/", OmniViews.mislibros, name='mislibros'),
    path('registro/', OmniViews.registro, name="registro"),
    path('registrarUsuario/', OmniViews.registrarUsuario),
    path("import_csv/", OmniViews.import_csv)
]
