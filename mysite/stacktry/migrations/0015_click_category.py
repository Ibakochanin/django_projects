# Generated by Django 4.2.3 on 2023-10-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0014_lesson_grappling_participation_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="click",
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
    ]
