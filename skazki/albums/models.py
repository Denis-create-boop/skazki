from django.db import models


class Albums(models.Model):
    
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    date = models.DateTimeField(auto_now_add=True)
    date_realeese = models.DateField(verbose_name="Дата выхода")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="albums_images", blank=True, null=True, verbose_name="Изображение"
    )
    listen_url = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на альбом")

    class Meta:
        db_table = "albums"
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"
        ordering = ("-date",)

    def __str__(self):
        return self.name


class Songs(models.Model):
    
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    author_text = models.CharField(max_length=150, blank=True, null=True, verbose_name="Автор текста")
    author_music = models.CharField(max_length=150, blank=True, null=True, verbose_name="Автор музыки")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    listen_url = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на песню")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="songs_images", blank=True, null=True, verbose_name="Изображение"
    )
    videofile = models.FileField(upload_to='song_videos', blank=True, null=True, verbose_name="Видео")
    album = models.ForeignKey(
        to=Albums, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Альбом"
    )
    date_realeese = models.DateField(blank=True, null=True, verbose_name="Дата выхода")
    text = models.TextField(blank=True, null=True, verbose_name="Текст песни")

    class Meta:
        db_table = "songs"
        verbose_name = "песню"
        verbose_name_plural = "песни"
        ordering = ("id",)

    def __str__(self):
        return self.name
    
    
class Singles(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    author_text = models.CharField(max_length=150, blank=True, null=True, verbose_name="Автор текста")
    author_music = models.CharField(max_length=150, blank=True, null=True, verbose_name="Автор музыки")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    listen_url = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на песню")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="songs_images", blank=True, null=True, verbose_name="Изображение"
    )
    videofile = models.FileField(upload_to='song_videos', blank=True, null=True, verbose_name="Видео")

    date_realeese = models.DateField(blank=True, null=True, verbose_name="Дата выхода")
    text = models.TextField(blank=True, null=True, verbose_name="Текст песни")

    class Meta:
        db_table = "singles"
        verbose_name = "single"
        verbose_name_plural = "singles"
        ordering = ("id",)

    def __str__(self):
        return self.name
