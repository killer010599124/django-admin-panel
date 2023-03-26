# Generated by Django 4.1.6 on 2023-03-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branchen",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("b_id", models.PositiveIntegerField()),
                ("sprach_id", models.PositiveIntegerField()),
                ("text", models.CharField(max_length=255)),
                ("cnsort", models.CharField(blank=True, max_length=10, null=True)),
                ("messe_text", models.CharField(max_length=255)),
                ("beschreibung", models.TextField(blank=True, null=True)),
                ("google", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "branchen", "managed": False,},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TradeFair",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(default="title name", max_length=255, null=True),
                ),
                ("b_id", models.PositiveIntegerField()),
                (
                    "image1",
                    models.ImageField(blank=True, null=True, upload_to="static/small"),
                ),
                (
                    "image2",
                    models.ImageField(blank=True, null=True, upload_to="static/large"),
                ),
            ],
            options={"ordering": ["id"],},
        ),
    ]
