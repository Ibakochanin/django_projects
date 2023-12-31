# Generated by Django 4.2.3 on 2023-10-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0011_lesson_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="grappling_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="lesson",
            name="jiu_jitsu_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="lesson",
            name="kick_boxing_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="lesson",
            name="yoga_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
