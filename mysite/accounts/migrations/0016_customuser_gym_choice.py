# Generated by Django 4.2.3 on 2023-11-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_customuser_content_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="gym_choice",
            field=models.CharField(
                choices=[("Kix", "Kix"), ("Iwade", "Iwade"), ("Both", "Both")],
                default="Kix",
                max_length=20,
            ),
        ),
    ]