# Generated by Django 3.1.4 on 2021-01-13 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210113_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='posts',
        ),
    ]
