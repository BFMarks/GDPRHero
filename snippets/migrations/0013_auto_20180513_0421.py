# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20180513_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='inboundemail',
            name='emailSentToUS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inboundemail',
            name='properEmail',
            field=models.BooleanField(default=True),
        ),
    ]
