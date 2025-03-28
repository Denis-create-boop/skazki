from django.shortcuts import render
from main.models import News, Concerts, Info



def news(request):

    news = News.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Новости",
        "news" : news,
        "concerts": concerts,
        "info_text": "Свежие новости:",
    }
    
    return render(request, "main/news.html", context=context)



def about(request):
    concerts = Concerts.objects.all()
    info = Info.objects.all()
    context = {
        "title": "Сказки Черного Города - О нас",
        "content": "О нас",
        "concerts": concerts,
        "info": info,
        "info_text": 'Информация о группе "Сказки Черного Города"',
    }

    return render(request, "main/about.html", context)


def details(request, concert_slug):
    concert = Concerts.objects.get(slug=concert_slug)
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Подробнее о концерте",
        "concert": concert,
        "concerts": concerts,
        "flug": True,
        "info_text": f"Подробная информация о концерте | {concert}",
    }
    return render(request, "main/details.html", context=context)


def afisha(request):
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Афиша",
        "concerts": concerts,
        "flug" : False,
        "info_text": "Афиша концертов:",
    }
    return render(request, "main/details.html", context=context)