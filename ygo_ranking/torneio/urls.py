from django.urls import path
from . import views
urlpatterns =[
    path('novo_torneio/' , views.novo_torneio, name = 'novo_torneio'),
    path('listar_torneio/' , views.listar_torneio, name = 'listar_torneio'),
    path('acessar_torneio/<str:identificador>/' , views.acessar_torneio, name = 'acessar_torneio'),
    path('gerar_os/<str:identificador>/' , views.gerar_os, name = 'gerar_os'),
    ]