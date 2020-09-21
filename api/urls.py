from rest_framework.routers import DefaultRouter

from .views import MangaViewSet


router = DefaultRouter()
router.register("mangas", MangaViewSet, basename="manga")


app_name = "api"
urlpatterns = []
urlpatterns += router.urls
