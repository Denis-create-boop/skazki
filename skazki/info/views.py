from django.shortcuts import render
from main.models import Concerts


def info(request):
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - свяжитесь с нами",
        "concerts": concerts,
    }
    return render(request, 'info/info.html', context=context)
