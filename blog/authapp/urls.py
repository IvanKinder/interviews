from django.contrib import admin
from django.urls import path

from authapp.views import register

app_name = 'authapp'


urlpatterns = [
    # path('login/', LoginView.as_view()),
    path('register/', register, name='register'),
]
