from django.contrib import admin
from django.urls import path

from songs import views

app_name = 'songs'

urlpatterns = [
    path("", views.songs, name="songs"),
    path("detail_song<slug:song_slug>", views.detail_song, name="detail_song"),
]