from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Film(models.Model):
    name = models.CharField(max_length=32, verbose_name='название')
    source = models.TextField(blank=True, verbose_name='ссылка на фильм')

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='фильм')
    created_at = models.DateTimeField(default=now, verbose_name='дата создания')
    comment = models.TextField(blank=True, verbose_name='комментарий')


class Star(models.Model):

    count_of_stars = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='фильм')
    stars = models.CharField(max_length=1, blank=True, choices=count_of_stars, verbose_name='количество звёздочек')