from django.shortcuts import render
from rest_framework import generics

from mainapp.serializers import QuestionDetailSerializer, PollDetailSerializer


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer
