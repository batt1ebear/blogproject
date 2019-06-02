# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190602_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
