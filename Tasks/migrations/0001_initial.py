# Generated by Django 5.2 on 2025-04-10 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category_name", models.CharField(verbose_name="name")),
                ("created_user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="created_user", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Tasks",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(verbose_name="title")),
                ("content", models.TextField(verbose_name="content")),
                ("time", models.TimeField(default="08:00", verbose_name="time")),
                ("repeat_days", models.CharField(blank=True, verbose_name="r_days")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="author", to=settings.AUTH_USER_MODEL)),
                ("category", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="category", to="Tasks.categories")),
            ],
        ),
    ]
