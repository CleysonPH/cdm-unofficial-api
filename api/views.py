from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from mangas.models import Author, Designer, Genre, Manga, Type

from .serializers import (
    AuthorSerializer,
    DesignerSerializer,
    GenreSerializer,
    MangaSerializer,
    TypeSerializer,
)


class MangaViewSet(viewsets.ModelViewSet):
    lookup_field = "cdm_id"
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class DesignerViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = DesignerSerializer
    queryset = Designer.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class AuthorMangas(APIView):
    def get(self, request, author, format=None):
        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(author__name=author)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)


class DesignerMangas(APIView):
    def get(self, request, designer, format=None):
        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(designer__name=designer)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)
