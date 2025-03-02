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


