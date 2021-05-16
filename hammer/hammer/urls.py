from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from authapp.views import login, tmp_code, user, ReferalUserAPIView, obtain_auth_token

router = DefaultRouter()
router.register('users', ReferalUserAPIView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', login, name='auth'),
    path('tmp_code/', tmp_code, name='tmp_code'),
    path('user/', user, name='user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-auth/', login, name='auth'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
