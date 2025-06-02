from django.shortcuts import render, get_object_or_404
from galery.models import CategoriesImages, Images
from main.models import Concerts

from datetime import datetime


def galery(request):
    categories = CategoriesImages.objects.all()
    images = Images.objects.all()
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    context = {
        "title": "Сказки Чёрного Города - Галерея",
        "categories": categories,
        "images": images,
        "concerts": concerts,
        "info_text": "Галерея",
    }
    return render(request, 'galery/galery.html', context=context)


