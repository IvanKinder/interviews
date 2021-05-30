from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from filmapp.models import Film, Comment, Star
from filmapp.serializers import FilmSerializer, CommentSerializer, CommentsOfFilmSerializer, StarSerializer


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
    queryset = Comment.objects.all()
    serializer_class = CommentsOfFilmSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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
