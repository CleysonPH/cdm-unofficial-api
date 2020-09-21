from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, AuthorViewSet


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")
router.register("authors", AuthorViewSet, basename="author")


app_name = "api"
urlpatterns = []
urlpatterns += router.urls
