# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-07 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_awardsmerch_projectmerch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='profile',
        ),
    ]
