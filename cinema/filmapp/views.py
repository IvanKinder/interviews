from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from filmapp.models import Film, Comment, Star
from filmapp.serializers import FilmSerializer, CommentSerializer, CommentsOfFilmSerializer, StarSerializer, \
    UserRegistrSerializer, StarAddSerializer


class FilmListView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        comments = Comment.objects.filter(film=instance.id)
        serializer = CommentsOfFilmSerializer(comments, many=True)
        return Response(serializer.data)


class CommentListView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CommentsOfFilmView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = CommentSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        comments = Comment.objects.filter(film=instance.id)
        serializer = CommentsOfFilmSerializer(comments, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        comment = Comment.objects.create(user=request.user, film=instance, comment=request.data['comment'])
        comment.save()
        return Response(serializer.data)


class StarsListView(ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Star.objects.filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data._mutable = True
        data.__setitem__('user', str(request.user.id))
        data._mutable = False
        serializer = StarAddSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer().data, status=status.HTTP_201_CREATED, headers=headers)


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    @classmethod
    def get_extra_actions(cls):
        return []