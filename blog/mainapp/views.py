from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.forms import PostForm
from mainapp.models import Post, Category, PostToCategory


class PostListView(ListView):
    model = Post
    template_name = 'mainapp/index.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Home'
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'mainapp/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Blog | Post'
        return context


class PostUserView(ListView):
    model = Post
    context_object_name = 'user_posts'
    ordering = ['-created_at']
    paginate_by = 10
    template_name = 'mainapp/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Posts'
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Post'
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(user=self.request.user, name=self.request.POST['name'], text=self.request.POST['text'], picture=request._files['picture'])
        post.save()
        return HttpResponseRedirect('/posts/')


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_delete.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'mainapp/categories.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Categories'
        return context


class CategoryCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Post'
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(user=self.request.user, name=self.request.POST['name'], text=self.request.POST['text'], picture=request._files['picture'])
        post.save()
        return HttpResponseRedirect('/posts/')


class CategoryUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context


class CategoryDeleteView(DeleteView):
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_delete.html'


class PostsInCategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'mainapp/category.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['title'] = f'Blog | Category'
        # context['posts'] = Post.objects.filter(pk=PostToCategory.objects.get())
        return context
