from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

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
        mangas = Manga.objects.filter(author__name=author)
        serializer = MangaSerializer(mangas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
