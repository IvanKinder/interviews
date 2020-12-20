from django.contrib import admin

from mainapp.models import Question, Poll, Answer

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Answer)
