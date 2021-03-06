# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-12 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180611_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductShareLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(blank=True, choices=[('facebook', 'Facebook'), ('google-plus', 'Google+'), ('twitter', 'Twitter'), ('email', 'Email')], max_length=25, null=True)),
                ('sharelink', models.URLField(blank=True, max_length=300, null=True)),
                ('create', models.DateTimeField(blank=True, null=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Share Link',
                'verbose_name_plural': 'Share Links',
            },
        ),
    ]
