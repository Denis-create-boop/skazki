from django.contrib import admin
from django.urls import path

from albums import views

app_name = 'albums'

urlpatterns = [
    path("", views.albums, name="albums"),
    path("details_album/<slug:album_slug>/", views.details_album, name="details_album"),
    path("details_single/<slug:song_slug>/", views.details_song, name="details_single"),
    path("details_song/<slug:song_slug>/<slug:album_slug>/", views.details_song, name="details_song"),
]