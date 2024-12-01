from django.urls import path
from . import views
urlpatterns =[
    path('', views.duelists, name = 'duelists'),
    path('update_duelist/', views.update_duelist, name = 'update_duelist')
]