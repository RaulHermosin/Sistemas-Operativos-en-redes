from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('registrar/', views.añadir),
    path('borrar/', views.borrar),
    path('actualizar/', views.actualizar),
]