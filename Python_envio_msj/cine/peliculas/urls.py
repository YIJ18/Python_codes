from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='lista'),
    path('agregar/', views.agregar_pelicula, name='agregar'),
]
