# Generated by Django 4.2.3 on 2023-10-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_customuser_grappling_count_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="grappling_count",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="jiu_jitsu_count",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="kick_boxing_count",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="yoga_count",
        ),
    ]