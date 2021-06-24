from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название категории')


class Tag(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название тега')


class Task(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название задачи')
    deadline = models.DateField(blank=True, verbose_name='Крайний срок выполнения')
    done = models.BooleanField(default=False, verbose_name='Выполнена')
    created_at = models.DateTimeField(default=now, verbose_name='Создана')
    updated_at = models.DateTimeField(default=now, verbose_name='Изменена')
    is_active = models.BooleanField(default=True, verbose_name='Активна')


class CategoryTask(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')


class TagTask(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
