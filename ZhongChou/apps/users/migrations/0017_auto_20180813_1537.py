# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180813_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile_tem',
            options={'verbose_name': '临时信息', 'verbose_name_plural': '临时信息'},
        ),
    ]
