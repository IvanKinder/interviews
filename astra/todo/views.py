import os

import openpyxl
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from todo.models import Category, Tag, Task, CategoryTask, TagTask
from todo.serializers import CategorySerializer, TagSerializer, TaskSerializer, CategoryTaskSerializer, \
    TagTaskSerializer
from todo.utils import export_to_file


class CategoryViewSet(ModelViewSet):
    """контроллер категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    """контроллер тегов"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(ModelViewSet):
    """контроллер задач"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryTaskViewSet(ModelViewSet):
    """контроллер связи категорий с задачами"""
    queryset = CategoryTask.objects.all()
    serializer_class = CategoryTaskSerializer


class TagTaskViewSet(ModelViewSet):
    """контроллер связи тегов с задачами"""
    queryset = TagTask.objects.all()
    serializer_class = TagTaskSerializer


def get_task_data(task_pk):
    """функция сбора данных задачи"""
    task_to_save = Task.objects.get(pk=task_pk)
    fields = ['name', 'deadline', 'description', 'done', 'created_at', 'updated_at', 'is_active']
    file_name = f'{Task.objects.get(pk=task_pk).name}'
    return task_to_save, fields, file_name


class TaskExport(APIView):
    """контроллер экспорта данных задачи в файл"""

    def get(self, request, pk):
        task = get_task_data(pk)
        export_to_file(task=task[0], fields=task[1], file_name=task[2])
        return Response('Файл сохранен!')


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def task_import(request, filename):
    """Функция импорта задачи из файла в корне проекта"""

    try:
        path = os.path.join(os.path.dirname(__file__), f'../{filename}')
        wb = openpyxl.load_workbook(path)
        sheet = wb.active

        Task.objects.create(name=sheet['A2'].value, deadline=sheet['B2'].value, description=sheet['C2'].value,
                            done=sheet['D2'].value, created_at=sheet['E2'].value, updated_at=sheet['F2'].value,
                            is_active=sheet['G2'].value)

        if 'format' in request.GET.keys():
            return Response(f'Добавлена задача из файла {filename}')
        else:
            return HttpResponse(f'Добавлена задача из файла {filename}')
    except Exception:
        return HttpResponse(f'Некорректные данные в файле {filename}')
