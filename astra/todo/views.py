from rest_framework.viewsets import ModelViewSet

from todo.models import Category, Tag, Task, CategoryTask, TagTask
from todo.serializers import CategorySerializer, TagSerializer, TaskSerializer, CategoryTaskSerializer, \
    TagTaskSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryTaskViewSet(ModelViewSet):
    queryset = CategoryTask.objects.all()
    serializer_class = CategoryTaskSerializer


class TagTaskViewSet(ModelViewSet):
    queryset = TagTask.objects.all()
    serializer_class = TagTaskSerializer
