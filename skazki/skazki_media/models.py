from django.db import models

class Skazki_media(models.Model):
    
    name = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="skazki_media_image", height_field=None, width_field=None, max_length=None, blank=True, 
                              null=True, verbose_name="Изображение")
    videofile = models.FileField(upload_to="skazki_media_video", verbose_name="Видео")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "skazki_media"
        verbose_name = "Медиа"
        verbose_name_plural = "Медиа"
        ordering = ("-date",)

    def __str__(self):
        return self.name