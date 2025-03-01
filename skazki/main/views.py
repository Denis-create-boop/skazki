from django.shortcuts import render
from main.models import News
from django.core.paginator import Paginator


def index(request):

    news = News.objects.all()
    context = {
        "title": "Сказки черного города - Главная",
        "news" : news,
    }
    
    return render(request, "main/index.html", context=context)



def about(request):
    context = {
        "title": "Сказки черного города - О нас",
        "content": "О нас",
    }

    return render(request, "main/about.html", context)
