from rest_framework.serializers import HyperlinkedModelSerializer

from todo.models import Category, Tag, Task, CategoryTask, TagTask


class CategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class CategoryTaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = CategoryTask
        fields = '__all__'


class TagTaskSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TagTask
        fields = '__all__'
