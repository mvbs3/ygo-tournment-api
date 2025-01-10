from django.urls import path
from . import views
urlpatterns =[
    path('novo_torneio/' , views.novo_torneio, name = 'novo_torneio'),
    path('listar_torneio/' , views.listar_torneio, name = 'listar_torneio'),
    path('torneio/<str:identificador>/' , views.torneio, name = 'torneio'),
    ]