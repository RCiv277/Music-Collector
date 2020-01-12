from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(model.models):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    duration = models.TimeField()
    date = models.DateField()
    artists = models.ManyToManyField(Artist, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': song.id})
    
    
class Artist(model.models):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs, blank=True)
    
    
    
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'artist_id': artist.id})