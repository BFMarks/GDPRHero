# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20180521_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='adjust_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='amplitude_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='appsflyer_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='branch_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='braze_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='customer_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='mixpanel_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apps',
            name='urbanairship_bool',
            field=models.BooleanField(default=False),
        ),
    ]
