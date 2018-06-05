# Generated by Django 2.0.5 on 2018-06-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_dataprocessors_processor_bool_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='customer_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dataprocessors',
            name='processor_bool_name',
            field=models.TextField(default='customer_user_id', max_length=100),
        ),
    ]