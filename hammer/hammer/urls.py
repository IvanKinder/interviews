from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
# from graphene_django.tests import schema_view
from rest_framework.routers import DefaultRouter

from authapp.views import login, tmp_code, user, ReferalUserAPIView, obtain_auth_token

router = DefaultRouter()
router.register('user', ReferalUserAPIView, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', login, name='auth'),
    path('tmp_code/', tmp_code, name='tmp_code'),
    path('user/', user, name='user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
