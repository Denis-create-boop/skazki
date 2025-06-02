from django.shortcuts import render
from main.models import News, Concerts, Info
from datetime import datetime



def news(request):

    news = News.objects.all()
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    delete_concerts = Concerts.objects.filter(date__lt=datetime.now())
    delete_concerts.delete()
    
    context = {
        "title": "Сказки Чёрного Города - Новости",
        "news" : news,
        "concerts": concerts,
        "info_text": "Свежие новости:",
    }
    
    return render(request, "main/news.html", context=context)



def about(request):
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    info = Info.objects.all()
    context = {
        "title": "Сказки Чёрного Города - О нас",
        "content": "О нас",
        "concerts": concerts,
        "info": info,
        "info_text": 'Информация о группе "Сказки Чёрного Города"',
    }

    return render(request, "main/about.html", context)


def details(request, concert_slug):
    concert = Concerts.objects.get(slug=concert_slug)
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Чёрного Города - Подробнее о концерте",
        "concert": concert,
        "concerts": concerts,
        "flug": True,
        "info_text": f"Подробная информация о концерте | {concert}",
    }
    return render(request, "main/details.html", context=context)


def afisha(request):
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    context = {
        "title": "Сказки Чёрного Города - Афиша",
        "concerts": concerts,
        "flug" : False,
        "info_text": "Афиша концертов:",
    }
    return render(request, "main/details.html", context=context)