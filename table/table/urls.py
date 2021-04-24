from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp.views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('frontend.urls')),
    path('', include(router.urls)),
    # url(r'^api/auth/', include('rest_auth.urls')),
    # url(r'api/', include('frontend.apiurls')),
]
