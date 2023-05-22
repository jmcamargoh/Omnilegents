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
from django.urls import path, include
from Omni import views as OmniViews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', OmniViews.home, name="home"),
    path("libros/", OmniViews.libros, name="libros"), #Para acceder a esta es el mismo enlace con /libros
    path("mislibros/", OmniViews.mislibros, name='mislibros'),
    path("cambiarPagLeidas/<int:pk>/",OmniViews.cambiarPagLeidas,name="cambiarPagLeidas"),
    path('calificar_libro/<int:libro_pk>/', OmniViews.calificar_libro, name='calificar_libro'),
    path('recomendar-libros/', OmniViews.recomendar_libros, name='recomendar_libros'),
    
    path("import_csv/", OmniViews.import_csv),
    path('randomizarGeneros/',OmniViews.randomizarGeneros, name = "randomizarGeneros"),
    path('', include('accounts.urls')),
    path('agregarlibro/<int:libro_id>/', OmniViews.agregarLibro, name='agregarLibro'),

    path("lista_notas/", OmniViews.lista_notas, name="lista_notas"), 
    path("nota/<int:pk>/", OmniViews.detalle_nota, name="detalle_nota"), 
    path("nota/crear/", OmniViews.crear_nota, name="crear_nota"), 

    path('nota/editar/<int:pk>/', OmniViews.editar_nota, name='editar_nota'),
    path('nota/eliminar/<int:pk>/', OmniViews.eliminar_nota, name='eliminar_nota'),

    path('retosylogros/',OmniViews.retosylogros, name="retosylogros"),
    path('retosylogros/retos/',OmniViews.retos  , name = "retos"),
    path('retosylogros/logros/',OmniViews.logros  , name = "logros"),

    path('recordatorios/',OmniViews.recordatorios,name="recordatorios"),
    path("recordatorio/<int:pk>/", OmniViews.detalle_recordatorio, name="detalle_recordatorio"), 
    path("recordatorio/crear/", OmniViews.crear_recordatorio, name="crear_recordatorio"),
    path('recordatorio/eliminar/<int:pk>/', OmniViews.eliminar_recordatorio, name='eliminar_recordatorio'),

    path('reviews/', OmniViews.leer_reviews, name="leer_reviews"),
    path('reviews/crear/', OmniViews.crear_review, name="crear_review"),
    path('misreviews/', OmniViews.mis_reviews, name="mis_reviews"),
    path('eliminar_review/<int:pk>', OmniViews.eliminar_review, name="eliminar_review"),
    path('editar_review/<int:pk>', OmniViews.editar_review, name="editar_review"),
]
