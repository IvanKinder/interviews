from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics

from mainapp.models import Poll, Question
from mainapp.serializers import PollDetailSerializer, QuestionDetailSerializer, PollListSerializer, \
    AnswerDetailSerializer, QuestionListSerializer


# def pollview(request, pk):
#     print(Poll.question_list(pk))


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PollListView(generics.ListAPIView):
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        request = self.request
        poll_pk = str(request)[-4]
        # poll = request.query_params.get('poll')
        # self.queryset = Question.objects.filter(poll_id=request.)
        self.queryset = Question.objects.filter(poll=poll_pk)
        return self.queryset


    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
# class AnswerCreateView(generics.CreateAPIView):
#     serializer_class = AnswerDetailSerializer
