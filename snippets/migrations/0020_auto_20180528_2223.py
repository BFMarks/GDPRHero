# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 22:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0019_auto_20180528_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 28, 22, 23, 1, 960450, tzinfo=utc)),
        ),
    ]
