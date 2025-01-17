from django.urls import path
from . import views
urlpatterns =[
    path('', views.duelists, name = 'duelists'),
    path('update_duelist/', views.update_duelist, name = 'update_duelist'),
    path('add_deck/', views.add_deck, name="add_deck"),
    path('update_deck/<int:id>', views.update_deck, name = 'update_deck'),
    path('delete_deck/<int:id>', views.delete_deck, name = 'delete_deck'),
    path('atualizar_duelist/<int:id>', views.atualizar_duelist, name="atualizar_duelist"),
    ]