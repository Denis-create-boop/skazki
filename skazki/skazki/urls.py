
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("user/", include("users.urls", namespace="user")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("info/", include("info.urls", namespace="info")),
    path("songs/", include("songs.urls", namespace="songs")),
    path("merch_shop/", include("merch_shop.urls", namespace="merch_shop")),
    path("galery/", include("galery.urls", namespace="galery")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
