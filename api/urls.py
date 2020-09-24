from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    MangaViewSet,
    AuthorViewSet,
    DesignerViewSet,
    GenreViewSet,
    TypeViewSet,
    AuthorMangas,
    DesignerMangas,
    GenreMangas,
    TypeMangas,
    TelegramUserViewSet,
    SubiscribeTelegramUser,
)


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")
router.register("authors", AuthorViewSet, basename="author")
router.register("designers", DesignerViewSet, basename="designer")
router.register("genres", GenreViewSet, basename="genre")
router.register("types", TypeViewSet, basename="type")

router.register("telegramusers", TelegramUserViewSet, basename="telegramuser")


app_name = "api"
urlpatterns = [
    path("authors/<str:name>/mangas/", AuthorMangas.as_view(), name="author-mangas"),
    path(
        "designers/<str:name>/mangas/",
        DesignerMangas.as_view(),
        name="designer-mangas",
    ),
    path("genres/<str:name>/mangas/", GenreMangas.as_view(), name="genre-mangas"),
    path("types/<str:name>/mangas/", TypeMangas.as_view(), name="type-mangas"),
    path(
        "telegramusers/<str:chat_id>/subscribe/<str:cdm_id>/",
        SubiscribeTelegramUser.as_view(),
        name="subscribe",
    ),
]
urlpatterns += router.urls
