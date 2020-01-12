from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs_index, name='songs_index'),
    path('artists/', views.artists_index, name='artists_index'),
    
    path('songs/<int:pk>', views.song_detail, name='song_detail'),
    path('artists/<int:pk>', views.artists_index, name='artist-detail'),
    
    path('songs/create', views.SongCreate.as_view() , name='create')
    path('artists/create', views.ArtistCreate.as_view() , name='create')
    
    path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_detail'),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist-detail'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('test', views.home, name='home'),
]