from django.shortcuts import render, get_object_or_404
from galery.models import CategoriesImages, Images


def galery(request):
    categories = CategoriesImages.objects.all()
    images = Images.objects.all()
    for category in categories:
        print(category)
    for img in images:
        print(img.category)
    context = {
        "title": "Сказки Черного Города - Галерея",
        "categories": categories,
        "images": images,
    }
    return render(request, 'galery/galery.html', context=context)


