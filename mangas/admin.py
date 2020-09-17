from django.contrib import admin

from .models import Manga, Author, Designer, Genre, Type


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_year", "status", "author", "designer")
    search_fields = ("title", "author")
    list_filter = ("status", "types", "genres", "author", "designer")


admin.site.register(Author)
admin.site.register(Designer)
admin.site.register(Genre)
admin.site.register(Type)
