from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.forms import PostForm, CategoryForm, SearchForm, ContactsForm
from mainapp.models import Post, Category, PostToCategory, Tag, PostToTag


class PostListView(ListView):
    """Представление для просмотра всех статей"""
    model = Post
    template_name = 'mainapp/index.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Home'
        return context


class PostDetailView(DetailView):
    """Представление для просмотра конкретной статьи"""
    model = Post
    context_object_name = 'post'
    template_name = 'mainapp/post.html'

    def get_context_data(self, **kwargs):
        """Добавление в context data тегов"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Blog | Post'
        context['tags'] = []
        try:
            for post_bind_tag in PostToTag.objects.filter(post_id=self.request.resolver_match[2]['pk']):
                context['tags'].append(Tag.objects.filter(pk=post_bind_tag.id)[0])
        except Exception as e:
            pass
        return context


class PostUserView(ListView):
    """Представление для отображения и редактирования статей текущего пользователя"""
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
    """Представление для создания статьи"""
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Post'
        return context

    def post(self, request, *args, **kwargs):
        tags = self.request.POST['tags'].split('#')
        print(tags)
        try:
            post = Post.objects.create(user=self.request.user, name=self.request.POST['name'],
                                       text=self.request.POST['text'], picture=request._files['picture'])
        except Exception:
            post = Post.objects.create(user=self.request.user, name=self.request.POST['name'],
                                       text=self.request.POST['text'])
        post.save()
        for tag in tags:
            if tag != '':
                tag_obj = Tag.objects.create(name=tag)
                tag_obj.save()
                tag_bind_post = PostToTag.objects.create(post=post, tag=tag_obj)
                tag_bind_post.save()

        return HttpResponseRedirect('/posts/')

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts/'
    template_name = 'mainapp/post_delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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


def post_search(request):
    form = SearchForm()
    tags = None
    results = []
    if 'tags' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            tags = form.cleaned_data['tags'].split('#')
            for tag in tags:
                if tag != '':
                    try:
                        for tag in Tag.objects.filter(name=tag):
                            results.append(PostToTag.objects.filter(tag_id=tag)[0])
                    except Exception as e:
                        pass

    return render(request,
                  'mainapp/search.html',
                  {'form': form,
                   'query': tags,
                   'results': results})


def contacts(request):
    form = ContactsForm()
    results = request.GET
    print(results)  # имитация обратной связи

    return render(request,
                  'mainapp/contacts.html',
                  {'form': form,
                   'results': results})
