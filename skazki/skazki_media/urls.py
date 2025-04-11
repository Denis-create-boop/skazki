from django.contrib import admin
from django.urls import path

from skazki_media import views

app_name = "skazki_media"

urlpatterns = [
    path("", views.skazki_media, name="skazki_media"),
]