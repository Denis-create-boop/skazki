from django.shortcuts import render
from songs.models import Songs
from main.models import Concerts



def songs(request):
    songs = Songs.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Релизы",
        "songs": songs,
        "concerts": concerts,
    }
    
    return render(request, "songs/songs.html", context=context)

def detail_song(request, song_slug):
    detail_about_song = Songs.objects.get(slug=song_slug)
    concerts = Concerts.objects.all()
    context = {
        "title": f"Сказки Черного Города - {detail_about_song.name}",
        "song": detail_about_song,
        "concerts": concerts,
    }
    return render(request, "songs/detail_song.html", context=context)