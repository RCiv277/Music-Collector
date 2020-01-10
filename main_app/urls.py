from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs_index, name='songs_index'),
    path('artists/', views.artists_index, name='artists_index'),
    path('songs/', views.home, name='home'),
    path('', views.home, name='home'),
    path('', views.home, name='home'),
]