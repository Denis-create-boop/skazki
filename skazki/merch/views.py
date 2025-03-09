from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from merch.models import Products
from merch.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get('q', None)

    if query:
        merch = q_search(query)
    else:
        merch = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        merch = Products.objects.filter(category__slug=category_slug)
        merch = merch.filter(discount__gt=0)
    if order_by and order_by != "default":
        merch = Products.objects.filter(category__slug=category_slug)
        merch = merch.order_by(order_by)

    paginator = Paginator(merch, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Сказки Черного города - Каталог",
        "merch": current_page,
        "slug_url": category_slug,
    }
    return render(request, "merch/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "merch/product.html", context=context)
