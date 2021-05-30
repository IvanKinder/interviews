from django.contrib.auth.models import User
from rest_framework import serializers
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
        fields = ('created_at', 'comment',)


class StarSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Star
        fields = ('id', 'film', 'stars',)


class StarAddSerializer(ModelSerializer):

    class Meta:
        model = Star
        fields = ('user', 'film', 'stars',)


class CommentsOfFilmSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('user', 'created_at', 'comment',)


class UserRegistrSerializer(ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user

