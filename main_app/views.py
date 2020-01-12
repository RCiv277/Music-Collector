from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Song , Artist


# Create your views here.

def home(request): 
    return render(request, 'home.html')


@login_required
def songs_index(request):
    song = Song.objects.filter(user = request.user)    
    return render(request, 'songs/index.html' , 'songs' : songs)


class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    fields = ['name', 'genre' , 'duration', 'date']

class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = '/songs/'


@login_required
def artists_index(request):
    return render(request, 'artists/index.html' , 'artists' : artists)

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    fields = ['name']
    
class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = '/artists/'
    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

