# Generated by Django 2.0.6 on 2018-07-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20180730_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]