# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophome', '0011_auto_20180613_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactuspage',
            name='corporate_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactuspage',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
