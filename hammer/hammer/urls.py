from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authapp.views import login

router = DefaultRouter()
# router.register('auth', login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', login, name='auth'),
]
