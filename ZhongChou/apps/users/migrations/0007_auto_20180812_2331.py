# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_idcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='accounttype',
            field=models.IntegerField(choices=[(1, '商业公司'), (2, '个体工商户'), (3, '个人经营'), (4, '政府及非营利组织')], default=3, verbose_name='账户类型'),
        ),
    ]
