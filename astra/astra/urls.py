from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import CategoryViewSet, TagViewSet, TaskViewSet, CategoryTaskViewSet, TagTaskViewSet, TaskExportAsCSV

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)
router.register('task', TaskViewSet)
router.register('categorytask', CategoryTaskViewSet)
router.register('tagtask', TagTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/export/<int:pk>/', TaskExportAsCSV.as_view())
]
