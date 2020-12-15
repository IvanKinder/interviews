from django.shortcuts import render
from rest_framework import generics
from mainapp.permissions import IsAdmin

from mainapp.models import Question, Poll
from mainapp.serializers import QuestionDetailSerializer, PollDetailSerializer, QuestionListSerializer, PollListSerializer


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer
    # permission_classes = (IsAdmin, )


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()


class PollListView(generics.ListAPIView):
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()


