from django.shortcuts import render
from skazki_media.models import Skazki_media

def skazki_media(request):
    videos = Skazki_media.get.all()
    context = {
        "title": "Сказки Черного Города - Медиа",
        "info_text": "Медиа",
        "videos": videos,
    }
    return render(request, 'skazki_media/skazki_media.html', context=context)
