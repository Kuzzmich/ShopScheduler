# Generated by Django 2.0.6 on 2018-07-29 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180729_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='break',
            options={'ordering': ['time_start']},
        ),
    ]
