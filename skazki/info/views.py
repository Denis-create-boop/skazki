from django.shortcuts import render
from main.models import Concerts
from info.models import Persons, Addresses


def info(request):
    concerts = Concerts.objects.all()
    persons = Persons.objects.all()
    addresses = Addresses.objects.all()
    context = {
        "title": "Сказки Чёрного Города - Контактная информация",
        "concerts": concerts,
        "persons": persons,
        "addresses": addresses,
        "info_text": "Контактная информация",
    }
    return render(request, 'info/info.html', context=context)
