from django.contrib import admin

from merch_shop.models import Categories, Products

# admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "image"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "quantity",
        "price",
        "discount",
    ]
    list_editable = ["quantity", "price", "discount",]
    search_fields = ["name", "description",]
    list_filter = [
        "quantity", 
        "discount", 
        "category",
    ]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        ("price", "discount"),
        "quantity",
        "image"
    ]


