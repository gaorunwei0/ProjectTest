# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_orderinfo_return_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='is_del',
            field=models.BooleanField(default=False, verbose_name='是否被删除'),
        ),
    ]