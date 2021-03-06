# Generated by Django 3.1.5 on 2021-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='male',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='updateDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.TextField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
