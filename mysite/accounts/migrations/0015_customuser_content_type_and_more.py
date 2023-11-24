# Generated by Django 4.2.3 on 2023-11-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_customuser_belt_customuser_member_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="content_type",
            field=models.CharField(
                help_text="The MIMEType of the file", max_length=256, null=True
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.BinaryField(editable=True, null=True),
        ),
    ]