from django.conf.urls import url
from django.urls import re_path

from frontend import views

urlpatterns = re_path('', url(r'auth/permissions/', views.permissions, name='permissions'),)
