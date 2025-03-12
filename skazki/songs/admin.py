from django.contrib import admin
from songs.models import Songs

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "date",
        "date_realeese",
        "album_list",
    ]
    search_fields = ["name", "description", "date", "date_realeese",]

    fields = [
        "name",
        "slug",
        "description",
        "image",
        "date_realeese",
        "about_song",
        "album_list",
    ]
