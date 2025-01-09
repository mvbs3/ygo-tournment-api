from django.urls import path
from . import views
urlpatterns =[
    path('novo_torneio/' , views.novo_torneio, name = 'novo_torneio'),
    ]