from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from filmapp.views import FilmListView, CommentListView, CommentsOfFilmView, StarsListView, RegistrUserView

router = DefaultRouter()
router.register('commentfilm', CommentsOfFilmView)
router.register('stars', StarsListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('accounts/', include('rest_framework.urls', namespace='rest_framework_auth')),
    path('reg/', RegistrUserView.as_view(), name='reg'),
    path('films/', FilmListView.as_view({'get': 'list'}), name='films'),
]
