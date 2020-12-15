from rest_framework import serializers

from mainapp.models import Question, Poll


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'poll', 'question_type')


class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('name', 'is_active')
