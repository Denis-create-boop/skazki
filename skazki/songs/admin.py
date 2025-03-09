from django.contrib import admin
from songs.models import Songs

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "date",
    ]
    search_fields = ["name", "description", "date",]

    fields = [
        "name",
        "slug",
        "description",
        "image"
    ]
