# Generated by Django 5.2.1 on 2025-05-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("responses", "0033_alter_teamtemperature_default_tz"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wordcloudimage",
            name="word_hash",
            field=models.CharField(max_length=64),
        ),
    ]
