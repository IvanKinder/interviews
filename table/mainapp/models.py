from django.db import models


class Book(models.Model):
    name = models.TextField(max_length=32, verbose_name='Название')
    author = models.TextField(max_length=32, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Год выпуска')
    in_stock = models.BooleanField(default=True, verbose_name='Наличие')
    price = models.IntegerField(verbose_name='Цена')
