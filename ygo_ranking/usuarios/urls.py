
from django.urls import path
from . import views
urlpatterns =[
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('plataforma/', views.plataforma, name = 'plataforma'),
    path('meu_perfil/', views.meu_perfil, name = 'meu_perfil'),
    ]