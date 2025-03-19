from django.shortcuts import render, get_object_or_404
from galery.models import CategoriesImages, Images
from main.models import Concerts


def galery(request):
    categories = CategoriesImages.objects.all()
    images = Images.objects.all()
    concerts = Concerts.objects.all()
    context = {
        "title": "Сказки Черного Города - Галерея",
        "categories": categories,
        "images": images,
        "concerts": concerts,
    }
    return render(request, 'galery/galery.html', context=context)


