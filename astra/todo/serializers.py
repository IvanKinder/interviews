from rest_framework.serializers import HyperlinkedModelSerializer

from todo.models import Category, Tag, Task, CategoryTask, TagTask


class CategorySerializer(HyperlinkedModelSerializer):
    """сериалайзер для категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(HyperlinkedModelSerializer):
    """сериалайзер для тегов"""

    class Meta:
        model = Tag
        fields = '__all__'


class TaskSerializer(HyperlinkedModelSerializer):
    """сериалайзер для задач"""

    class Meta:
        model = Task
        fields = '__all__'


class CategoryTaskSerializer(HyperlinkedModelSerializer):
    """сериалайзер для связи категорий с задачами"""

    class Meta:
        model = CategoryTask
        fields = '__all__'


class TagTaskSerializer(HyperlinkedModelSerializer):
    """сериалайзер для связи тегов с задачами"""

    class Meta:
        model = TagTask
        fields = '__all__'
