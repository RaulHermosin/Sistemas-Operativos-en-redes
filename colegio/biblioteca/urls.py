from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('crearlibro/', views.crearlibro),
    path('verlibro/', views.verlibro),
    path('borrarlibro/', views.borrarlibro),
]