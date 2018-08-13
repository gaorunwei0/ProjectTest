# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 08:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180812_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile_tem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('accounttype', models.IntegerField(choices=[(1, '商业公司'), (2, '个体工商户'), (3, '个人经营'), (4, '政府及非营利组织')], default=3, verbose_name='账户类型')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('phonenum', models.IntegerField(blank=True, null=True, verbose_name='手机号')),
                ('idcard', models.CharField(blank=True, max_length=18, null=True, verbose_name='身份证')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]