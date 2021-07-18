from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель статьи"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=32, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активна')


class MediaPost(models.Model):
    """Модель картинок для статьи"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')
    number = models.IntegerField(verbose_name='Порядковый номер')
    media_link = models.CharField(max_length=128, verbose_name='Ссылка на изображение')


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=32, verbose_name='Название категории')
    description = models.CharField(max_length=128, blank=True, verbose_name='Описание категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активна')


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField(max_length=32, verbose_name='Название тега')


class PostToCategory(models.Model):
    """Связь статьи и категории"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')


class PostToTag(models.Model):
    """Связь статьи и тега"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
