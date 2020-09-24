# Generated by Django 3.1.1 on 2020-09-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mangas", "0007_auto_20200923_1243"),
        ("bot", "0002_auto_20200923_2035"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="telegramuser",
            options={
                "ordering": ("created_at",),
                "verbose_name": "Usuário Telegram",
                "verbose_name_plural": "Usuários Telegram",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
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
                (
                    "manga",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mangas.manga",
                        verbose_name="Manga",
                    ),
                ),
                (
                    "telegram_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bot.telegramuser",
                        verbose_name="Telegram User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Inscrição",
                "verbose_name_plural": "Inscrições",
                "ordering": ("created_at",),
            },
        ),
    ]
