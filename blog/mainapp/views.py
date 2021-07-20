from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.forms import PostForm, CategoryForm
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
        try:
            post = Post.objects.create(user=self.request.user, name=self.request.POST['name'],
                                       text=self.request.POST['text'], picture=request._files['picture'])
        except Exception:
            post = Post.objects.create(user=self.request.user, name=self.request.POST['name'],
                                       text=self.request.POST['text'])
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
    context_object_name = 'categories'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Categories'
        return context


class CategoryCreateView(CreateView):
    form_class = CategoryForm
    model = Category
    success_url = '/categories/'
    template_name = 'mainapp/category_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Category'
        return context


class CategoryUpdateView(UpdateView):
    form_class = CategoryForm
    model = Category
    success_url = '/categories/'
    template_name = 'mainapp/category_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/categories/'
    template_name = 'mainapp/category_delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostsInCategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'mainapp/category.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Blog | Category'
        context['data'] = PostToCategory.objects.filter(category_id=self.request.__dict__['resolver_match'][2]['pk'])
        return context


class AddPostToCategoryListView(ListView):
    model = Post
    success_url = '/categories/'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10
    template_name = 'mainapp/post_to_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Add To Category'
        context['category'] = self.request.__dict__['resolver_match'][2]['pk']
        return context


class AddPostToCategoryView(ListView):
    model = PostToCategory
    success_url = '/categories/'
    context_object_name = 'posts_to_category'
    # ordering = ['-created_at']
    paginate_by = 10
    template_name = 'mainapp/add_post.html'

    def get_context_data(self, **kwargs):
        pk_data = self.request.__dict__['resolver_match'][2]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Add Post'

        try:
            added_post = PostToCategory.objects.create(post_id=pk_data['pk'], category_id=pk_data['cat_pk'])
            added_post.save()
        except Exception:
            context['data'] = 'Статья уже в этой категории'
        return context
