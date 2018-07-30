# Generated by Django 2.0.6 on 2018-07-29 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180729_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerecord',
            name='schedule_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_record', to='shop.Schedule', verbose_name='Schedule'),
        ),
    ]
