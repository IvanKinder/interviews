from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer, HyperlinkedModelSerializer

from filmapp.models import Film, Comment, Star


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class FilmSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class StarSerializer(ModelSerializer):
    film = FilmSerializer()

    class Meta:
        model = Star
        fields = ('film', 'stars',)


class CommentsOfFilmSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('user', 'created_at', 'comment',)

