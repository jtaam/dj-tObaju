# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('icon', models.CharField(help_text='fa-hearts , ref: https://fontawesome.bootstrapcheatsheets.com/', max_length=50)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'advantage',
                'verbose_name_plural': 'advantages',
            },
        ),
        migrations.AlterModelOptions(
            name='topslider',
            options={'verbose_name': 'Top Slider', 'verbose_name_plural': 'Top Slider'},
        ),
    ]