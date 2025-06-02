from django.shortcuts import render
from main.models import Concerts
from albums.models import Albums, Songs, Singles

from datetime import datetime


def albums(request):
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    albums = Albums.objects.all()
    singles = Singles.objects.all()
    
    context = {
        "title": "Сказки Чёрного Города - Релизы",
        "concerts": concerts,
        "albums": albums,
        "info_text": "Релизы",
        "singles": singles,

    }
    
    return render(request, 'albums/albums.html', context=context)


def details_album(request, album_slug):
    songs = Songs.objects.filter(album__slug=album_slug)
    detail_about_album = Albums.objects.get(slug=album_slug)
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    context = {
        "title": f"Сказки Чёрного Города - {detail_about_album.name}",
        "album": detail_about_album,
        "songs": songs,
        "concerts": concerts,
        "info_text": detail_about_album.name,
        "slug": album_slug,
        "flag": True,
    }
    return render(request, "albums/details_album.html", context=context)


def details_song(request, song_slug, album_slug=None):
    
    if album_slug:
        songs_in_album = Songs.objects.filter(album__slug=album_slug)
        song = Songs.objects.get(slug=song_slug)
        album = Albums.objects.get(slug=album_slug)
    else:
        songs_in_album = None
        song = Singles.objects.get(slug=song_slug)
        album = None
        
    
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    context = {
        "title": f"Сказки Чёрного Города - {song.name}",
        "song": song,
        "album": album,
        "concerts": concerts,
        "info_text": song.name,
        "songs_in_album": songs_in_album,
        "flag": False,

    }
    return render(request, "albums/details_album.html", context=context)