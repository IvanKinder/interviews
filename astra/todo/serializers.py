from rest_framework.serializers import HyperlinkedModelSerializer

from todo.models import Category, Tag, Task, CategoryTask, TagTask


# сериалайзер для категорий
class CategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# сериалайзер для тегов
class TagSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


# сериалайзер для задач
class TaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


# сериалайзер для связи категорий с задачами
class CategoryTaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = CategoryTask
        fields = '__all__'


# сериалайзер для связи тегов с задачами
class TagTaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TagTask
        fields = '__all__'
