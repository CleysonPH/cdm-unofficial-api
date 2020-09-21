from rest_framework import viewsets

from .serializers import MangaSerializer
from mangas.models import Manga


class MangaViewSet(viewsets.ModelViewSet):
    lookup_field = "cdm_id"
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()
