from django.shortcuts import render
from skazki_media.models import Skazki_media
from main.models import Concerts

from datetime import datetime

def skazki_media(request):
    videos = Skazki_media.objects.all()
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    context = {
        "title": "Сказки Чёрного Города - Медиа",
        "info_text": "Медиа",
        "concerts": concerts,
        "videos": videos,
    }
    return render(request, 'skazki_media/skazki_media.html', context=context)
