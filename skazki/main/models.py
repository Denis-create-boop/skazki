from django.db import models
from django.urls import reverse

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
    videofile = models.FileField(upload_to='news_videos', blank=True, null=True, verbose_name="Видео")
    name_address_1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название ссылки")
    address_1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
    name_address_2 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название ссылки")
    address_2 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
    name_address_3 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название ссылки")
    address_3 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
    name_address_4 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название ссылки")
    address_4 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка")
    

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
    place = models.CharField(max_length=250, verbose_name="Место проведения")
    image = models.ImageField(
        upload_to="concerts_images", blank=True, null=True, verbose_name="Изображение"
    )
    tickets = models.CharField(max_length=150, verbose_name="Билеты")
    
    
    class Meta:
        db_table = "concerts"
        verbose_name = "концерт"
        verbose_name_plural = "концерты"
        ordering = ("-date",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:concerts", kwargs={"concerts_slug": self.slug})
    
    def get_month(self):
        months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь",
            
        }
        
        return months[self.date.month]
    
    def get_weekday(self):
        days = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье",
        }
        
        return days[self.date.weekday()]
    
    
class Info(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Заголовок")
    date = models.DateTimeField(blank=True, null=True, verbose_name="дата")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="info_images", blank=True, null=True, verbose_name="Изображение"
    )
    videofile = models.FileField(upload_to='info_videos',blank=True, null=True, verbose_name="Видео")
    
    
    class Meta:
        db_table = "info_about_group"
        verbose_name = "событие"
        verbose_name_plural = "события"
        ordering = ("-date",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:about", kwargs={"info_slug": self.slug})