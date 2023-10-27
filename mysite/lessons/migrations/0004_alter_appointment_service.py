# Generated by Django 4.2.3 on 2023-09-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0003_alter_appointment_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="service",
            field=models.CharField(
                choices=[
                    (
                        "Profound conversation with Ivar sama",
                        "Profound conversation with Ivar sama",
                    ),
                    ("Nursing care", "Nursing care"),
                    ("Medical social services", "Medical social services"),
                    (
                        "Homemaker or basic assistance care",
                        "Homemaker or basic assistance care",
                    ),
                ],
                default="Profound conversation with Ivar sama",
                max_length=50,
            ),
        ),
    ]
