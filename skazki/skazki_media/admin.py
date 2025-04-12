from django.contrib import admin
from skazki_media.models import Skazki_media

@admin.register(Skazki_media)
class SkazkiMediaAdmin(admin.ModelAdmin):
    search_fields = ["name", "date",]

    fields = [
        "name",
        "description",
        "image",
        "videofile",
    ]
