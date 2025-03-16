from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from merch_shop.models import Products, Categories
from merch_shop.utils import q_search


def merch_shop(request):
    page = request.GET.get("page", 1)
    merch_shop = Categories.objects.all()
        
    categories = Categories.objects.all()
    paginator = Paginator(merch_shop, 9)
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Сказки Черного Города - Каталог",
        "categories": categories,
        "merch_shop": current_page,

    }
    return render(request, 'merch_shop/merch_categories.html', context=context)


def get_products(request, category_slug):
    
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    merch_shop = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        merch_shop = Products.objects.filter(category__slug=category_slug)
        merch_shop = merch_shop.filter(discount_gt=0)

    paginator = Paginator(merch_shop, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Сказки Черного Города - " + category_slug,
        "products": current_page,
        "slug_url": category_slug,
        
    }
    return render(request, 'merch_shop/merch.html', context=context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "merch_shop/product.html", context=context)