# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-02 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20190602_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='url',
        ),
    ]
