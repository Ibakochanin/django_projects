# Generated by Django 4.2.3 on 2023-11-09 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0030_participationcount_monthly_count_b_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="participationcount",
            old_name="grappling_count",
            new_name="basic_count",
        ),
        migrations.RenameField(
            model_name="participationcount",
            old_name="kick_boxing_count",
            new_name="competition_count",
        ),
        migrations.RenameField(
            model_name="participationcount",
            old_name="yoga_count",
            new_name="free_mat_count",
        ),
    ]
