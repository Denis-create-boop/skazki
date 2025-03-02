from django.db import models
from django.urls import reverse
from datetime import datetime

class News(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Заголовок")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="news_images", blank=True, null=True, verbose_name="Изображение"
    )
    

    class Meta:
        db_table = "news"
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ("-date",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:news", kwargs={"news_slug": self.slug})


class Concerts(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Заголовок")
    date = models.DateTimeField()
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    
    
    class Meta:
        db_table = "concerts"
        verbose_name = "концерт"
        verbose_name_plural = "концерты"
        ordering = ("-date",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:concerts", kwargs={"concerts_slug": self.slug})