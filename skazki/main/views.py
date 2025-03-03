from django.shortcuts import render
from main.models import News, Concerts



def news(request):

    news = News.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки черного города - Главная",
        "news" : news,
        "concerts": concerts,
    }
    
    return render(request, "main/news.html", context=context)



def about(request):
    context = {
        "title": "Сказки черного города - О нас",
        "content": "О нас",
    }

    return render(request, "main/about.html", context)


def details(request, concert_slug):
    concert = Concerts.objects.get(slug=concert_slug)
    concerts = Concerts.objects.all()
    context = {
        "title": "Подробнее о концерте",
        "concert": concert,
        "concerts": concerts,
        "flug": True,
    }
    return render(request, "main/details.html", context=context)


def afisha(request):
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки черного города - Афиша",
        "concerts": concerts,
        "flug" : False,
    }
    return render(request, "main/details.html", context=context)