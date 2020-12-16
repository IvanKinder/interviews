from django.contrib.auth.models import User
from rest_framework import serializers

from mainapp.models import Question, Poll


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'poll', 'question_type')


class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('name', 'is_active')


class UserPollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

