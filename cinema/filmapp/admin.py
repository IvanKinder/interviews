from django.contrib import admin

from filmapp.models import Film, Comment, Star


admin.site.register(Film)
admin.site.register(Comment)
admin.site.register(Star)