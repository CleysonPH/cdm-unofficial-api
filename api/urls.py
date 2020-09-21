from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, AuthorViewSet, DesignerViewSet


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")
router.register("authors", AuthorViewSet, basename="author")
router.register("designers", DesignerViewSet, basename="designer")


app_name = "api"
urlpatterns = []
urlpatterns += router.urls
