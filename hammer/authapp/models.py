from django.contrib.auth.models import User
from django.db import models


class ReferalUser(User):
    """ расширенный стандартный юзер """

    phone_number = models.IntegerField(verbose_name='номер телефона', unique=True)
    code = models.CharField(max_length=6, verbose_name='инвайт-код', unique=True)
    invited_users = models.JSONField(verbose_name='приглашенные пользователи', blank=True, null=True)
