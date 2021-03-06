# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophome', '0012_auto_20180613_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='StayInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('googleplus', models.URLField(blank=True, null=True)),
                ('emailus', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Stay In Touch',
                'verbose_name_plural': 'Stay In Touch',
            },
        ),
    ]
