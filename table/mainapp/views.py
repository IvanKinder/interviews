from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Book
from mainapp.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset[::-1]
