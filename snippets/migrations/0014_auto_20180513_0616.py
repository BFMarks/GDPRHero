# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_auto_20180513_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboundemail',
            name='inboundEmail',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
