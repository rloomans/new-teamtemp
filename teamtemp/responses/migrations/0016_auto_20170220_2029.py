# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0015_auto_20170201_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordcloudimage',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='wordcloudimage',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wordcloudimage',
            name='word_hash',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]