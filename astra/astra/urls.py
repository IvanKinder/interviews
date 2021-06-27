from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import CategoryViewSet, TagViewSet, TaskViewSet, CategoryTaskViewSet, TagTaskViewSet, TaskExport

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)
router.register('task', TaskViewSet)
router.register('categorytask', CategoryTaskViewSet)
router.register('tagtask', TagTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # стандартная админка
    path('api/', include(router.urls)),  # точка входа api
    path('api/export/<int:pk>/', TaskExport.as_view())  # url для экспорта задачи по id
]
