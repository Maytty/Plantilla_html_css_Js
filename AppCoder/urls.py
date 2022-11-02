from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('equipos/', views.equipos, name='Equipos'),
    path('torneos/', views.torneos, name='Torneos'),
    path('juegos/', views.juegos, name='Juegos'),
    path('busqueda_juego', views.busqueda_juego, name='Busqueda_Juego'),
    path('buscar/', views.buscar, name='Buscar'),     
]