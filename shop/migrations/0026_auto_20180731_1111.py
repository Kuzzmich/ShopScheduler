# Generated by Django 2.0.6 on 2018-07-31 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20180731_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerecord',
            name='schedule_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_records', to='shop.Schedule', verbose_name='Schedule'),
        ),
    ]