from . import views
from django.urls import path

app_name = 'ipl'

urlpatterns = [
    path('add_players/', views.add_players, name='add_players'),
    path('', views.home, name='home'),
    path('players/', views.players, name='players'),
    path('<int:player_id>/details/', views.details, name='details'),





]
