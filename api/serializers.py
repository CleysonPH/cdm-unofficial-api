from rest_framework import serializers

from mangas.models import Manga, Author, Designer, Genre, Type


class MangaSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="name", queryset=Author.objects.all(), allow_null=True
    )
    designer = serializers.SlugRelatedField(
        slug_field="name", queryset=Designer.objects.all(), allow_null=True
    )
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Genre.objects.all(), allow_null=True
    )
    types = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Type.objects.all(), allow_null=True
    )

    class Meta:
        model = Manga
        exclude = ("created_at", "modified_at")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ("created_at", "modified_at")


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        exclude = ("created_at", "modified_at")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ("created_at", "modified_at")


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        exclude = ("created_at", "modified_at")
