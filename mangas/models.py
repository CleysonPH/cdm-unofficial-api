from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        "Data de Criação", auto_now=False, auto_now_add=True
    )
    modified_at = models.DateTimeField(
        "Data de Modificação", auto_now=True, auto_now_add=False
    )

    class Meta:
        abstract = True


class Manga(BaseModel):
    STATUS_CHOICES = (
        (1, "Cancelado"),
        (2, "Completo"),
        (3, "Completo (Em Tradução)"),
        (4, "Em publicação"),
        (5, "Pausado"),
    )

    cdm_id = models.CharField(
        "CDM ID", max_length=255, blank=False, null=False, unique=True
    )
    title = models.CharField("Título", max_length=255, blank=False, null=False)
    link = models.URLField("Link", max_length=255, blank=False, null=False, unique=True)
    img_url = models.URLField("Imagem", max_length=255, blank=False, null=True)
    publish_year = models.IntegerField("Ano", blank=False, null=True)
    status = models.IntegerField(
        "Status", choices=STATUS_CHOICES, blank=False, null=True
    )
    author = models.ForeignKey(
        "mangas.Author",
        verbose_name="Autor",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    designer = models.ForeignKey(
        "mangas.Designer",
        verbose_name="Artista",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    genres = models.ManyToManyField("mangas.Genre", verbose_name="Gênero")
    types = models.ManyToManyField("mangas.Type", verbose_name="Tipos")
    summary = models.TextField("Resumo", blank=False, null=True)

    class Meta:
        verbose_name = "mangá"
        verbose_name_plural = "mangás"
        ordering = ("created_at",)

    def __str__(self):
        return self.title


class Author(BaseModel):
    name = models.CharField("Nome", max_length=125, unique=True)

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"
        ordering = ("created_at",)

    def __str__(self):
        return self.name


class Designer(BaseModel):
    name = models.CharField("Nome", max_length=125, unique=True)

    class Meta:
        verbose_name = "artista"
        verbose_name_plural = "artistas"
        ordering = ("created_at",)

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField("Nome", max_length=125, unique=True)

    class Meta:
        verbose_name = "gênero"
        verbose_name_plural = "gêneros"
        ordering = ("created_at",)

    def __str__(self):
        return self.name


class Type(BaseModel):
    name = models.CharField("Nome", max_length=125, unique=True)

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ("created_at",)

    def __str__(self):
        return self.name
