from django.db import models


    
class Persons(models.Model):
    name = models.CharField(max_length=250, verbose_name="ФИО")
    profession = models.CharField(max_length=250, blank=True, null=True, verbose_name="Профессия")
    description = models.TextField(verbose_name="Описание")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    name_address_1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название соцсети")
    address_1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на соцсеть")
    name_address_2 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название соцсети")
    address_2 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на соцсеть")
    name_address_3 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Название соцсети")
    address_3 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на соцсеть")

    
    class Meta:
        db_table = "persons"
        verbose_name = "человека"
        verbose_name_plural = "люди"
        ordering = ("id",)

    def __str__(self):
        return self.name
    
    

class Addresses(models.Model):
    
    name = models.CharField(max_length=250, verbose_name="Название")
    address = models.CharField(max_length=250, verbose_name="Ссылка")
    
    class Meta:
        db_table = "addresses"
        verbose_name = "ссылку"
        verbose_name_plural = "ссылки"
        ordering = ("id",)

    def __str__(self):
        return self.name