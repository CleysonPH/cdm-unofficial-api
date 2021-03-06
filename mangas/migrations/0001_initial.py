# Generated by Django 3.1.1 on 2020-09-17 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Modificação"
                    ),
                ),
                ("name", models.CharField(max_length=125, verbose_name="Nome")),
            ],
            options={
                "verbose_name": "autor",
                "verbose_name_plural": "autores",
            },
        ),
        migrations.CreateModel(
            name="Designer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Modificação"
                    ),
                ),
                ("name", models.CharField(max_length=125, verbose_name="Nome")),
            ],
            options={
                "verbose_name": "artista",
                "verbose_name_plural": "artistas",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Modificação"
                    ),
                ),
                ("name", models.CharField(max_length=125, verbose_name="Nome")),
            ],
            options={
                "verbose_name": "gênero",
                "verbose_name_plural": "gêneros",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Modificação"
                    ),
                ),
                ("name", models.CharField(max_length=125, verbose_name="Nome")),
            ],
            options={
                "verbose_name": "tipo",
                "verbose_name_plural": "tipos",
            },
        ),
        migrations.CreateModel(
            name="Manga",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Modificação"
                    ),
                ),
                ("cdm_id", models.CharField(max_length=255, verbose_name="CDM ID")),
                ("title", models.CharField(max_length=255, verbose_name="Título")),
                ("link", models.URLField(max_length=255, verbose_name="Link")),
                (
                    "img_url",
                    models.URLField(max_length=255, null=True, verbose_name="Imagem"),
                ),
                ("publish_year", models.IntegerField(null=True, verbose_name="Ano")),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Cancelado"),
                            (2, "Completo"),
                            (3, "Completo (Em Tradução)"),
                            (4, "Em publicação"),
                            (5, "Pausado"),
                        ],
                        verbose_name="Status",
                    ),
                ),
                ("summary", models.TextField(null=True, verbose_name="Resumo")),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mangas.author",
                        verbose_name="Autor",
                    ),
                ),
                (
                    "designer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mangas.designer",
                        verbose_name="Artista",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mangas.genre",
                        verbose_name="Gênero",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="mangas.type",
                        verbose_name="Tipo",
                    ),
                ),
            ],
            options={
                "verbose_name": "mangá",
                "verbose_name_plural": "mangás",
            },
        ),
    ]
