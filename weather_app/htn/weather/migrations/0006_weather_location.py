# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_weather_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='location',
            field=models.CharField(default='none', max_length=500),
        ),
    ]
