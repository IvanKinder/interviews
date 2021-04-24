from rest_framework.serializers import Serializer, HyperlinkedModelSerializer

from mainapp.models import Book


class BookSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
