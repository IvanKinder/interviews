from django.contrib import admin

from todo.models import Category, Tag, Task, CategoryTask, TagTask


# Добавление моделей в админку
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(CategoryTask)
admin.site.register(TagTask)
