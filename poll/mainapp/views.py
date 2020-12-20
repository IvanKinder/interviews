from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import generics

from mainapp.models import Poll, Question, Answer
from mainapp.serializers import PollDetailSerializer, QuestionDetailSerializer, PollListSerializer, \
    AnswerDetailSerializer, QuestionListSerializer


# def pollview(request, pk):
#     print(Poll.question_list(pk))
TMP_LIST = []


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
    # queryset = Question.objects.all()

    def get_queryset(self):
        poll_pk = self.kwargs['pk']
        self.queryset = Question.objects.filter(poll=poll_pk)
        return self.queryset


    def get_view_name(self):
        TMP_LIST.append(self.__dict__)
        if len(TMP_LIST) == 1:
            pk = TMP_LIST[0]
            view_name = Poll.objects.filter(pk=pk["kwargs"]["pk"])[0]
            return view_name
        if len(TMP_LIST) > 1:
            pk = TMP_LIST[-2]
            try:
                view_name = Poll.objects.filter(pk=pk["kwargs"]["pk"])[0]
                TMP_LIST.clear()
                return view_name
            except:
                pk = TMP_LIST[-1]
                view_name = Poll.objects.filter(pk=pk["kwargs"]["pk"])[0]
                TMP_LIST.clear()
                return view_name


    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AnswerDetailView(generics.CreateAPIView):
    serializer_class = AnswerDetailSerializer
    # queryset = Answer.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        print(self.request.__dict__['resolver_match'][2]['pk'])
        return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     poll_pk = self.kwargs['pk']
    #     self.queryset = Question.objects.filter(poll=poll_pk)
    #     return self.queryset

# class AnswerCreateView(generics.CreateAPIView):
#     serializer_class = AnswerDetailSerializer
