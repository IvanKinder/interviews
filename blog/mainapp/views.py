from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'mainapp/index.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Home'
        return context
