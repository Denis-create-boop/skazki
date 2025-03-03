from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.news, name="news"),
    path("about", views.about, name="about"),
    path("details/<slug:concert_slug>/", views.details, name="details"),
    path("afisha", views.afisha, name="afisha"),
]