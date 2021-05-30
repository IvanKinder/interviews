from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from filmapp.models import Film, Comment, Star


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class FilmSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class StarSerializer(ModelSerializer):

    class Meta:
        model = Star
        fields = '__all__'
