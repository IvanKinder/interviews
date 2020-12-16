from django.contrib import admin
from django.urls import path
from mainapp.views import *


app_name = 'Вопрос'
urlpatterns = [
    path('question/create/', QuestionCreateView.as_view()),
    path('question/', QuestionListView.as_view()),
    path('question/detail/<int:pk>/', QuestionDetailView.as_view()),
    path('poll/create/', PollCreateView.as_view()),
    path('poll/', PollListView.as_view()),
    path('user/poll/', UserPollListView.as_view()),
]
