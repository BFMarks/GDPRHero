# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0018_snippet_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='clever_tap_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='fabric_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='facebook_user_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='googleAnalytics_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snippet',
            name='optimizely_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
