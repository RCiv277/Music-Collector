from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs_index, name='songs_index'),
    path('artists/', views.artists_index, name='artists_index'),
    
    path('songs/<int:song_id>', views.song_detail, name='song_detail'),
    path('artists/<int:artist_id>', views.artist_detail, name='artist_detail'),
    
    path('songs/create', views.SongCreate.as_view() , name='song_create'),
    path('artists/create', views.ArtistCreate.as_view() , name='artist_create'),
    
    path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_delete'),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist_delete'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('test', views.home, name='home'),
]