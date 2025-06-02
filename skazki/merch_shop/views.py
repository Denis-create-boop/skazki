from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from merch_shop.models import Products, Categories
from main.models import Concerts

from datetime import datetime


def merch_shop(request):
    page = request.GET.get("page", 1)
    merch_shop = Categories.objects.all()
    concerts = Concerts.objects.filter(date__gte=datetime.now())
        
    categories = Categories.objects.all()
    paginator = Paginator(merch_shop, 4)
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Сказки Чёрного Города - Магазин",
        "categories": categories,
        "merch_shop": current_page,
        "concerts": concerts,
        "info_text": 'Магазин группы "Сказки Чёрного Города"',

    }
    return render(request, 'merch_shop/merch_categories.html', context=context)


def get_products(request, category_slug, name):
    
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    merch_shop = Products.objects.filter(category__slug=category_slug)
    concerts = Concerts.objects.filter(date__gte=datetime.now())

    if on_sale:
        merch_shop = Products.objects.filter(category__slug=category_slug)
        merch_shop = merch_shop.filter(discount_gt=0)

    paginator = Paginator(merch_shop, 9)
    current_page = paginator.page(int(page))

    context = {
        "title": "Сказки Чёрного Города - " + name,
        "products": current_page,
        "slug_url": category_slug,
        "concerts": concerts,
        "info_text": name,
        
    }
    return render(request, 'merch_shop/merch.html', context=context)


def product(request, product_slug, name):
    concerts = Concerts.objects.filter(date__gte=datetime.now())
    product = Products.objects.get(slug=product_slug)

    context = {
        "title": f"Сказки Чёрного Города - Магазин/{name}",
        "product": product,
        "concerts": concerts,
        "info_text": name,
        }
    return render(request, "merch_shop/product.html", context=context)