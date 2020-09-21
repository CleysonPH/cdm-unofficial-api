from rest_framework import serializers

from mangas.models import Manga, Author, Designer, Genre, Type


class MangaSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="name", queryset=Author.objects.all()
    )
    designer = serializers.SlugRelatedField(
        slug_field="name", queryset=Designer.objects.all()
    )
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Genre.objects.all()
    )
    types = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Type.objects.all()
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
