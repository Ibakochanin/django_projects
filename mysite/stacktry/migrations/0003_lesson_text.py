# Generated by Django 4.2.3 on 2023-10-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0002_lesson"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="text",
            field=models.TextField(null=True),
        ),
    ]
