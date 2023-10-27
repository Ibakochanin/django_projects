# Generated by Django 4.2.3 on 2023-10-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0004_click_lesson"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="day",
            field=models.CharField(
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                    ("Saturday", "Saturday"),
                    ("Sunday", "Sunday"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="spot",
            field=models.IntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                ],
                null=True,
            ),
        ),
    ]