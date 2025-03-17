from django.contrib import admin
from galery.models import CategoriesImages, Images


@admin.register(CategoriesImages)
class CategoriesImagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "data",
        "photograph"
    ]
    search_fields = ["name", "description", "data", "photograph",]

    fields = [
        "name",
        "slug",
        "description",
        "photograph",
    ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = [
        "image",
        "category",
    ]

    fields = [
        "image",
        "category",
    ]

    

