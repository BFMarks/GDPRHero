# Generated by Django 2.0.5 on 2018-06-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_auto_20180602_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='fabric_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='facebook_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='googleAnalytics_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='iterable_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='leanplum_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='optimizely_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='subparam1_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='subparam2_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='subparam3_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='urban_airship_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='adjust_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='amplitude_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='appsflyer_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='branch_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='braze_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='mixpanel_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='urbanairship_bool',
            field=models.BooleanField(default=True),
        ),
    ]