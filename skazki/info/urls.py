from django.contrib import admin
from django.urls import path

from info import views

app_name = "info"

urlpatterns = [
    path("", views.info, name="info"),
]
