# Generated by Django 4.2.3 on 2023-11-17 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0032_participationcount_black_jiu_jitsu_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="click",
            name="order",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
