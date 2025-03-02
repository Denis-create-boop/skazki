from django.contrib import admin
from django.urls import path

from merch import views

app_name = "merch"

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="news"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
