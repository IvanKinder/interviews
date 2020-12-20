from rest_framework import serializers

from mainapp.models import Poll, Question, Answer


class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'poll', 'question_type')


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('name',)


class AnswerDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = '__all__'


