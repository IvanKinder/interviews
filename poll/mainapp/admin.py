from django.contrib import admin

from mainapp.models import Question, Poll

admin.site.register(Question)
admin.site.register(Poll)
