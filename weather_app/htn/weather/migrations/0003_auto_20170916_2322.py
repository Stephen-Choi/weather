# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20170916_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
