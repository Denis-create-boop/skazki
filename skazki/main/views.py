from django.shortcuts import render
from main.models import News, Concerts, Info



def news(request):

    news = News.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного города - Новости",
        "news" : news,
        "concerts": concerts,
    }
    
    return render(request, "main/news.html", context=context)



def about(request):
    concerts = Concerts.objects.all()
    info = Info.objects.all()
    context = {
        "title": "Сказки Черного города - О нас",
        "content": "О нас",
        "concerts": concerts,
        "info": info,
    }

    return render(request, "main/about.html", context)


def details(request, concert_slug):
    concert = Concerts.objects.get(slug=concert_slug)
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного города - Подробнее о концерте",
        "concert": concert,
        "concerts": concerts,
        "flug": True,
    }
    return render(request, "main/details.html", context=context)


def afisha(request):
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного города - Афиша",
        "concerts": concerts,
        "flug" : False,
    }
    return render(request, "main/details.html", context=context)