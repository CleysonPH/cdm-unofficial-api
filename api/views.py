from rest_framework import viewsets

from .serializers import (
    MangaSerializer,
    AuthorSerializer,
    DesignerSerializer,
    GenreSerializer,
    TypeSerializer,
)
from mangas.models import Manga, Author, Designer, Genre, Type


class MangaViewSet(viewsets.ModelViewSet):
    lookup_field = "cdm_id"
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class DesignerViewSet(viewsets.ModelViewSet):
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