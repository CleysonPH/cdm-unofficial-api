from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, AuthorViewSet, DesignerViewSet, GenreViewSet


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")
router.register("authors", AuthorViewSet, basename="author")
router.register("designers", DesignerViewSet, basename="designer")
router.register("genres", GenreViewSet, basename="genre")


app_name = "api"
urlpatterns = []
urlpatterns += router.urls
