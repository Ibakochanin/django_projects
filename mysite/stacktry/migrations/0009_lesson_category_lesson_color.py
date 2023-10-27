# Generated by Django 4.2.3 on 2023-10-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0008_alter_lesson_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="category",
            field=models.CharField(
                choices=[
                    ("Jiu Jitsu", "Jiu Jitsu"),
                    ("Grappling", "Grappling"),
                    ("Kick Boxing", "Kick Boxing"),
                    ("Yoga", "Yoga"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="color",
            field=models.CharField(
                choices=[
                    ("sky", "Sky"),
                    ("green", "Green"),
                    ("yellow", "Yellow"),
                    ("purple", "Purple"),
                    ("pink", "Pink"),
                    ("light red", "Light Red"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
