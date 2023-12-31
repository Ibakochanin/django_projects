# Generated by Django 4.2.3 on 2023-11-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "stacktry",
            "0031_rename_grappling_count_participationcount_basic_count_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="participationcount",
            name="black_jiu_jitsu_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="participationcount",
            name="blue_jiu_jitsu_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="participationcount",
            name="brown_jiu_jitsu_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="participationcount",
            name="purple_jiu_jitsu_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="participationcount",
            name="white_jiu_jitsu_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
