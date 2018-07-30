# Generated by Django 2.0.6 on 2018-07-30 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='schedule_owner',
        ),
        migrations.AddField(
            model_name='schedule',
            name='shop_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shop.Shop', verbose_name='Schedule owner'),
            preserve_default=False,
        ),
    ]
