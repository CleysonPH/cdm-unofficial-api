from django.contrib import admin

from .models import Manga, Author, Designer, Genre, Type


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_year", "status", "author", "designer")
    search_fields = ("title",)
    list_filter = ("status", "types", "genres", "author", "designer")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
