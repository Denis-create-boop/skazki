from django.db import models

class Skazki_media(models.Model):
    
    name = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.TextField(blunk=True, null=True, verbose_name="Описание")
    videofile = models.FieldFile(upload_to="skazki_media", verbose_name="Видео")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "skazki_media"
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ("-date",)

    def __str__(self):
        return self.name