from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from propiedades import views

urlpatterns = [
    path('catalogo', views.catalogo, name="catalogo"),
    path('propiedad', views.detallePropiedad, name="propiedad"),
]

