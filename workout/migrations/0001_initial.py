# Generated by Django 4.2.6 on 2023-11-10 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import workout.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=50, primary_key="True", serialize=False
                    ),
                ),
                (
                    "config",
                    models.JSONField(default=workout.models.Exercise.exercise_default),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=50, primary_key="True", serialize=False
                    ),
                ),
                ("config", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutLog",
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
                ("date", models.DateField(default=datetime.date(2023, 11, 10))),
                ("set_logs", models.JSONField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]