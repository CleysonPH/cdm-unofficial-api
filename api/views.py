from rest_framework import viewsets

from .serializers import MangaSerializer, AuthorSerializer
from mangas.models import Manga, Author


class MangaViewSet(viewsets.ModelViewSet):
    lookup_field = "cdm_id"
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
