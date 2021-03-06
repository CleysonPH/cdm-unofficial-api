# Generated by Django 3.1.1 on 2020-09-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TelegramUser",
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
                ("chat_id", models.CharField(max_length=50, verbose_name="Chat ID")),
                (
                    "first_name",
                    models.CharField(max_length=100, null=True, verbose_name="Nome"),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Sobrenome"
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário Telegram",
                "verbose_name_plural": "Usuários Telegram",
            },
        ),
    ]
