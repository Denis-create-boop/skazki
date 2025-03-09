from django.shortcuts import render
from songs.models import Songs
from main.models import Concerts



def songs(request):
    songs = Songs.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки черного города - Релизы",
        "songs": songs,
        "concerts": concerts,
    }
    
    return render(request, "songs/songs.html", context=context)

def detail_song(request, song_slug):
    detail_about_song = Songs.objects.get(slug=song_slug)
    context = {
        "title": f"Сказки Черного города - {detail_about_song.name}",
        "song": detail_about_song,
    }
    return render(request, "songs/detail_song.html", context=context)