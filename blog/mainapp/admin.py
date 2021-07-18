from django.contrib import admin

from mainapp.models import Post, MediaPost, Category, Tag, PostToCategory, PostToTag


admin.site.register(Post)
admin.site.register(MediaPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostToCategory)
admin.site.register(PostToTag)
