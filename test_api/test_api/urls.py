from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/mainapp/', include('mainapp.urls')),
    path('accounts/', include('rest_framework.urls')),
]
