# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_favfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favfile',
            name='nums',
        ),
    ]
