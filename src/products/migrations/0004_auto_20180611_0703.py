# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180611_0637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorygroup',
            options={'verbose_name': 'Category Group', 'verbose_name_plural': 'Category Groups'},
        ),
        migrations.AddField(
            model_name='colours',
            name='color_code',
            field=models.CharField(blank=True, help_text='visit http://w3schools.com', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='colours',
            name='name',
            field=models.CharField(default='blue', max_length=20),
        ),
    ]
