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
        "image",
        "videofile",
        "name_address_1",
        "address_1",
        "name_address_2",
        "address_2",
        "name_address_3",
        "address_3",
        "name_address_4",
        "address_4",
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
        "videofile",
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