# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_accounttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_activation',
            field=models.BooleanField(default=False, verbose_name='是否认证'),
        ),
    ]
