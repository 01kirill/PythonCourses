from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from app.forms import RegisterForm, LoginForm
from app.models import Genre, Song

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def main_view(request):
    genres = Genre.objects.all()
    genre_id = request.GET.get('genre')
    query = request.GET.get('q')
    songs = Song.objects.all()
    if genre_id:
        songs = songs.filter(genre_id=genre_id)
    if query:
        songs = songs.filter(
            Q(title__icontains=query) |
            Q(artist__name__icontains=query)
        )

    return render(request, 'main.html', {
        'songs': songs,
        'genres': genres,
        'selected_genre': genre_id
    })

def artist_view(request):
    return render(request, 'artist.html')
