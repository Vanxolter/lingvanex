# Generated by Django 4.1.5 on 2023-01-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="parse_data",
            name="link",
            field=models.URLField(blank=True, null=True, verbose_name="link"),
        ),
    ]
