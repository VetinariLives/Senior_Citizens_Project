# Generated by Django 5.1.2 on 2024-10-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_merge_20241022_2159"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]
