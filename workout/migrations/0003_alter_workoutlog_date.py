# Generated by Django 4.2.7 on 2023-11-15 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workout", "0002_alter_workoutlog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workoutlog",
            name="date",
            field=models.DateField(default=datetime.date(2023, 11, 15)),
        ),
    ]
