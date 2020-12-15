from django.contrib.auth.models import AbstractUser
from django.db import models


class Poll(models.Model):
    name = models.CharField(verbose_name='Название опроса', max_length=25, unique=True)
    created_at = models.DateTimeField(verbose_name='Дата старта', auto_now=True)
    ended_at = models.DateTimeField(verbose_name='Дата окончания', blank=True, default=None)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    description = models.CharField(verbose_name='Описание', max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос', default=None)
    QUESTION_TYPES = (
        (1, 'Ответ текстом'),
        (2, 'Ответ с выбором одного варианта'),
        (3, 'Ответ с выбором нескольких вариантов'),
    )
    question_type = models.SmallIntegerField(verbose_name='Тип вопроса', choices=QUESTION_TYPES)
    question = models.CharField(verbose_name='Вопрос', max_length=100, unique=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return f'{self.question}; из опроса "{self.poll.name}"'


class PollUser(AbstractUser):
    def __str__(self):
        return self.username


class Answer(models.Model):
    user = models.ForeignKey(PollUser, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос', default=None)
    
