from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/crear_mascota/', views.crear_mascota, name='crear_mascota'),
]
