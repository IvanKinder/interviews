from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from todo.models import Category, Tag, Task, CategoryTask, TagTask
from todo.serializers import CategorySerializer, TagSerializer, TaskSerializer, CategoryTaskSerializer, \
    TagTaskSerializer
from todo.utils import export_to_csv


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


def get_task_data(task_pk):
    task_to_save = Task.objects.get(pk=task_pk)
    fields = ['name', 'deadline', 'description', 'done', 'created_at', 'updated_at', 'is_active']
    titles = ['name', 'deadline', 'description', 'done', 'created_at', 'updated_at', 'is_active']
    file_name = f'task.{now()}'
    return task_to_save, fields, titles, file_name


class TaskExportAsCSV(APIView):
    def get(self, request, pk):
        task = get_task_data(pk)
        export_to_csv(task=task[0], fields=task[1], titles=task[2], file_name=task[3])
        return Response('Файл сохранен!')
