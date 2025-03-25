from django.contrib import admin
from albums.models import Albums, Songs, Singles


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "date_realeese",
    ]
    search_fields = ["name", "description", "date", "date_realeese",]

    fields = [
        "name",
        "slug",
        "listen_url",
        "description",
        "image",
        "date_realeese",
    ]

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "date_realeese",
        "album",
    ]
    search_fields = ["name", "description", "date_realeese", "album",]

    fields = [
        "name",
        "slug",
        "listen_url",
        "author_text",
        "author_music",
        "description",
        "image",
        "date_realeese",
        "videofile",
        "album",
        "text",
    ]
    
    
@admin.register(Singles)
class SinglesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "date_realeese",
    ]
    search_fields = ["name", "description", "date_realeese",]
    fields = [
        "name",
        "slug",
        "listen_url",
        "author_text",
        "author_music",
        "description",
        "image",
        "date_realeese",
        "videofile",
        "text",
    ]