# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_apps_timeupdated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apps',
            options={},
        ),
        migrations.RemoveField(
            model_name='apps',
            name='created',
        ),
        migrations.RemoveField(
            model_name='apps',
            name='timeUpdated',
        ),
    ]
