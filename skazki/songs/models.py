from django.db import models
from django.urls import reverse

class Songs(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    date_realeese = models.DateField(verbose_name="Дата выхода")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    album_list = models.TextField(blank=True, null=True, verbose_name="Песни в альбоме")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    about_song = models.TextField(blank=True, null=True, verbose_name="Текст песни")
    image = models.ImageField(
        upload_to="song_images", blank=True, null=True, verbose_name="Изображение"
    )
    videofile = models.FileField(upload_to='song_videos', blank=True, null=True, verbose_name="Видео")
    

    class Meta:
        db_table = "songs"
        verbose_name = "песню"
        verbose_name_plural = "песни"
        ordering = ("-date",)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("songs:songs", kwargs={"songs_slug": self.slug})
    
    
    def get_song(self):
        names_songs = self.album_list.split()
        ls_name = []
        
        for i in range(2, len(names_songs) + 1, 3):
            ls_name.append(names_songs[i])
        result = []
            
        for i in range(1, len(ls_name) + 1):
            result.append([i, ls_name[i - 1]])
        
        return result
        
