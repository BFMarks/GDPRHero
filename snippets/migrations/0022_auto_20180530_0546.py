# Generated by Django 2.0.5 on 2018-05-30 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0021_auto_20180528_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inboundemail',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='inboundemail',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
