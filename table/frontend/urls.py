from django.conf.urls import url
from django.urls import re_path, path

from frontend import views

urlpatterns = [
    path('', views.index, name='index'),
]
