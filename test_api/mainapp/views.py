from django.shortcuts import render
from rest_framework import generics

from mainapp.models import Question, Poll
from mainapp.serializers import QuestionDetailSerializer, PollDetailSerializer, QuestionsListSerializer, \
    PollsListSerializer


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionsListSerializer
    queryset = Question.objects.all()


class PollListView(generics.ListAPIView):
    serializer_class = PollsListSerializer
    queryset = Poll.objects.all()


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
