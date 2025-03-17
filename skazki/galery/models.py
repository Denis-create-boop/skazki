from django.db import models


class CategoriesImages(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, unique=True, verbose_name="заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="описание")
    photograph = models.CharField(blank=True, null=True, verbose_name="фотограф")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    
    class Meta:
        db_table = "CategoryImages"
        verbose_name = "дата"
        verbose_name_plural = "дата"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    

    
class Images(models.Model):
    image = models.ImageField(
        upload_to="merch_products_images", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        to=CategoriesImages, on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        db_table = "images"
        verbose_name = "изображение"
        verbose_name_plural = "изображения"
        ordering = ("id",)
        
    def __str__(self):
        return "Картинка"




