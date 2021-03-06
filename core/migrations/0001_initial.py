# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-30 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='资源名称')),
                ('size', models.IntegerField(default=0, verbose_name='资源大小')),
                ('content_type', models.CharField(max_length=200, verbose_name='资源类型')),
                ('storage', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '资源管理',
                'verbose_name_plural': '资源管理',
            },
        ),
    ]
