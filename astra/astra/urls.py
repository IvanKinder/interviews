from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from todo.views import CategoryViewSet, TagViewSet, TaskViewSet, CategoryTaskViewSet, TagTaskViewSet, TaskExport, \
    task_import

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)
router.register('task', TaskViewSet)
router.register('categorytask', CategoryTaskViewSet)
router.register('tagtask', TagTaskViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # стандартная админка
    path('api/', include(router.urls)),  # точка входа api
    path('api/export/<int:pk>/', TaskExport.as_view()),  # url для экспорта задачи по id
    path('api/import/<str:filename>/', task_import),  # url для загрузки задачи из файла в корне проекта
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url для документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # url для документации
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # url для документации
    path("schema/", SpectacularAPIView.as_view(), name="schema"),  # url для выгрузки документации OpenApi 3
]
