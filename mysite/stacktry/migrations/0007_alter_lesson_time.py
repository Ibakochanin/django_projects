# Generated by Django 4.2.3 on 2023-10-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0006_lesson_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="time",
            field=models.CharField(max_length=9, null=True),
        ),
    ]
