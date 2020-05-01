from django.urls import path
from CowsAndBullsApp import views

app_name="CowsAndBullsApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('playgame/', views.playgame, name='playgame'),
]