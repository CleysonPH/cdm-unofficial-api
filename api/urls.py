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
)


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")
router.register("authors", AuthorViewSet, basename="author")
router.register("designers", DesignerViewSet, basename="designer")
router.register("genres", GenreViewSet, basename="genre")
router.register("types", TypeViewSet, basename="type")


app_name = "api"
urlpatterns = [
    path("authors/<str:author>/mangas/", AuthorMangas.as_view(), name="author-mangas"),
    path(
        "designers/<str:designer>/mangas/",
        DesignerMangas.as_view(),
        name="designer-mangas",
    ),
]
urlpatterns += router.urls
