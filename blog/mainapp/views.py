from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, UpdateView


class MainView(ListView):
    template_name = 'mainapp/index.html'
    model = User
