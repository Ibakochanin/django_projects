# Generated by Django 4.2.3 on 2023-10-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0012_lesson_grappling_participation_count_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="grappling_participation_count",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="jiu_jitsu_participation_count",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="kick_boxing_participation_count",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="participation_count",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="yoga_participation_count",
        ),
        migrations.AddField(
            model_name="click",
            name="grappling_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="click",
            name="jiu_jitsu_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="click",
            name="kick_boxing_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="click",
            name="yoga_participation_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
