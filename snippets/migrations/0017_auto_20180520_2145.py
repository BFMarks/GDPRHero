# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_auto_20180516_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='appsflyer_int',
        ),
        migrations.AddField(
            model_name='snippet',
            name='adjust_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='amplitude_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='branch_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='braze_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='customer_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='mixpanel_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='urbanairship_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
