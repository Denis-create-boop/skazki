from django.contrib import admin
from django.urls import path

from merch_shop import views

app_name = "merch_shop"

urlpatterns = [
    path("", views.merch_shop, name="merch_shop"),
    path("<slug:category_slug>/", views.products, name="products"),
    path("product/<slug:product_slug>/", views.product, name="product"),

]
