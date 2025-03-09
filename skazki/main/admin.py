from django.contrib import admin
from main.models import News, Concerts, Info

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
    
    
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "description", "date",]

    fields = [
        "name",
        "slug",
        "description",
        "date",
        "image",
    ]


@admin.register(Concerts)
class CorcertsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "description", "date", "place"]

    fields = [
        "name",
        "slug",
        "description",
        "place",
        "date",
        "image",
        "tickets",
    ]