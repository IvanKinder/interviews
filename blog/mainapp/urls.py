"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.views import PostListView, PostDetailView, PostUserView, PostCreateView, PostUpdateView, PostDeleteView, \
    CategoryListView, PostsInCategoryDetailView, CategoryCreateView, AddPostToCategoryView, AddPostToCategoryListView, \
    CategoryUpdateView, CategoryDeleteView, post_search, contacts

app_name = 'mainapp'

urlpatterns = [
                  path('', PostListView.as_view(), name='home'),
                  path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
                  path('posts/', PostUserView.as_view(), name='posts'),
                  path('categories/', CategoryListView.as_view(), name='categories'),
                  path('category/<int:pk>/', PostsInCategoryDetailView.as_view(), name='category'),
                  path('category_create/', CategoryCreateView.as_view(), name='category_create'),
                  path('updatecategory/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
                  path('deletecategory/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
                  path('create/', PostCreateView.as_view(), name='post_create'),
                  path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
                  path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
                  path('add_post_list/<int:pk>/', AddPostToCategoryListView.as_view(), name='add_post_list'),
                  path('add_post/<int:pk>/<int:cat_pk>/', AddPostToCategoryView.as_view(), name='add_post'),
                  path('search/', post_search, name='search'),
                  path('contacts/', contacts, name='contacts'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
