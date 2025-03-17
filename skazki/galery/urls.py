from django.urls import path
from galery import views

app_name = "galery"

urlpatterns = [
    path("", views.galery, name="galery"),

]