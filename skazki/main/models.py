from django.db import models
from django.urls import reverse

class News(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="merch_images", blank=True, null=True, verbose_name="Изображение"
    )
    

    class Meta:
        db_table = "news"
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:index", kwargs={"product_slug": self.slug})

