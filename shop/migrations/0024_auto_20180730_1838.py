# Generated by Django 2.0.6 on 2018-07-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20180730_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerecord',
            name='is_holiday',
            field=models.BooleanField(default=True, verbose_name='Is holiday'),
        ),
    ]
