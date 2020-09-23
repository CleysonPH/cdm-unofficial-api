from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from mangas.models import Author, Designer, Genre, Manga, Type
from bot.models import TelegramUser

from .serializers import (
    AuthorSerializer,
    DesignerSerializer,
    GenreSerializer,
    MangaSerializer,
    TypeSerializer,
    TelegramUserSerializer
)


class MangaViewSet(viewsets.ModelViewSet):
    lookup_field = "cdm_id"
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("title",)
    search_fields = ("title",)


class AuthorViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("name",)
    search_fields = ("name",)


class DesignerViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = DesignerSerializer
    queryset = Designer.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("name",)
    search_fields = ("name",)


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("name",)
    search_fields = ("name",)


class TypeViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("name",)
    search_fields = ("name",)


class AuthorMangas(APIView):
    def get(self, request, name, format=None):
        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(author__name=name)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)


class DesignerMangas(APIView):
    def get(self, request, name, format=None):
        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(designer__name=name)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)


class GenreMangas(APIView):
    def get(self, request, name, format=None):
        genre = get_object_or_404(Genre, name=name)

        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(genres__id=genre.id)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)


class TypeMangas(APIView):
    def get(self, request, name, format=None):
        type = get_object_or_404(Type, name=name)

        pagination = PageNumberPagination()
        mangas = Manga.objects.filter(types__id=type.id)
        result = pagination.paginate_queryset(mangas, request)
        serializer = MangaSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)


class TelegramUserViewSet(viewsets.ModelViewSet):
    lookup_field = "chat_id"
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()
