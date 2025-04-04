from django.db import models
from django.urls import reverse

class Categories(models.Model):
    
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="merch_categories_images", blank=True, null=True, verbose_name="Изображение"
    )

    class Meta:
        db_table = "category"
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("id",)

    def __str__(self):
        return self.name
    

    
class Products(models.Model):
    
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    buy_url = models.CharField(max_length=250, verbose_name="ссылка на товар")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="merch_products_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0, max_digits=7, decimal_places=0, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=100, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merch_shop:get_products", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"


    def sell_price(self):
        if self.discount:
            return int(self.price - self.price * self.discount / 100)
        return self.price
