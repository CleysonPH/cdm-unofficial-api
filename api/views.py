from rest_framework import viewsets

from .serializers import MangaSerializer, AuthorSerializer, DesignerSerializer
from mangas.models import Manga, Author, Designer


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
