from rest_framework.viewsets import ModelViewSet

from filmapp.models import Film, Comment
from filmapp.serializers import FilmSerializer, CommentSerializer


class FilmListView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class CommentListView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
