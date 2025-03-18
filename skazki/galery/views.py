from django.shortcuts import render, get_object_or_404
from galery.models import CategoriesImages, Images


def galery(request):
    categories = CategoriesImages.objects.all()
    images = Images.objects.all()
    context = {
        "title": "Сказки Черного Города - Галерея",
        "categories": categories,
        "images": images,
    }
    return render(request, 'galery/galery.html', context=context)


