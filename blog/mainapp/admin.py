from django.contrib import admin

from mainapp.models import Post, Category, Tag, PostToCategory, PostToTag


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostToCategory)
admin.site.register(PostToTag)
