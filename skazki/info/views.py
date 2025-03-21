from django.shortcuts import render
from main.models import Concerts


def info(request):
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Контактная информация",
        "concerts": concerts,
        "info_text": "Контактная информация",
    }
    return render(request, 'info/info.html', context=context)
