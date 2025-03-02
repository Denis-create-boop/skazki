from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.news, name="news"),
    path("about", views.about, name="about"),
]