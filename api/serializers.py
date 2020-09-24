from django.urls import reverse
from rest_framework import serializers

from mangas.models import Manga, Author, Designer, Genre, Type
from bot.models import TelegramUser, Subscription


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
    mangas = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ("name", "mangas")

    def get_mangas(self, obj):
        return reverse("api:author-mangas", kwargs={"name": obj.name})


class DesignerSerializer(serializers.ModelSerializer):
    mangas = serializers.SerializerMethodField()

    class Meta:
        model = Designer
        fields = ("name", "mangas")

    def get_mangas(self, obj):
        return reverse("api:designer-mangas", kwargs={"name": obj.name})


class GenreSerializer(serializers.ModelSerializer):
    mangas = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ("name", "mangas")

    def get_mangas(self, obj):
        return reverse("api:genre-mangas", kwargs={"name": obj.name})


class TypeSerializer(serializers.ModelSerializer):
    mangas = serializers.SerializerMethodField()

    class Meta:
        model = Type
        fields = ("name", "mangas")

    def get_mangas(self, obj):
        return reverse("api:type-mangas", kwargs={"name": obj.name})


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ("id", "chat_id", "first_name", "last_name")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("id", "telegram_user", "manga")


class TelegramUserSubscriptionSerializer(serializers.ModelSerializer):
    manga = MangaSerializer()

    class Meta:
        model = Subscription
        fields = ["manga"]
