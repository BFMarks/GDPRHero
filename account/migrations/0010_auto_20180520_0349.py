# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180520_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='store_url',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
