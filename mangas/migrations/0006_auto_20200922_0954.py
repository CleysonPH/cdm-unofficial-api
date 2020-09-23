# Generated by Django 3.1.1 on 2020-09-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mangas", "0005_auto_20200922_0908"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manga",
            name="status",
            field=models.IntegerField(
                choices=[
                    (1, "Cancelado"),
                    (2, "Completo"),
                    (3, "Completo (Em Tradução)"),
                    (4, "Em publicação"),
                    (5, "Pausado"),
                ],
                null=True,
                verbose_name="Status",
            ),
        ),
    ]