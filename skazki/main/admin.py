from django.contrib import admin
from main.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
    ]
    search_fields = ["name", "description",]

    fields = [
        "name",
        "slug",
        "description",
        "image"
    ]
