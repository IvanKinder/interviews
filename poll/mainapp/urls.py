from django.contrib import admin
from django.urls import path, include

from mainapp.views import PollCreateView, QuestionCreateView, PollDetailView, QuestionDetailView, PollListView, \
    QuestionListView, AnswerDetailView, AnswerListView, AnsweredPollsListView

urlpatterns = [
    path('poll/create/', PollCreateView.as_view()),
    path('poll/update/<pk>/', PollDetailView.as_view()),
    path('poll/list/', PollListView.as_view()),
    path('question/create/', QuestionCreateView.as_view()),
    path('question/update/<pk>/', QuestionDetailView.as_view()),
    path('poll/<pk>/', QuestionListView.as_view()),
    path('answer/', AnswerDetailView.as_view()),
    path('answer/list/', AnswerListView.as_view()),
    path('answer/poll/', AnsweredPollsListView.as_view()),
]
