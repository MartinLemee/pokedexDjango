from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pokemon/<int:number>/', views.pokemon, name="pokemon"),  
    path('pokedex/', views.pokedex, name="pokedex"),
]
