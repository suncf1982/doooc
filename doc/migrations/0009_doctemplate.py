# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-31 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0008_doc_download_times'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='模板名称')),
                ('storage', models.FileField(upload_to='templates/%Y/%m/%d/', verbose_name='存放位置')),
                ('preview_image', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='预览图')),
                ('usage_times', models.IntegerField(default=0, verbose_name='应用次数')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name_plural': '文档模板',
                'verbose_name': '文档模板',
            },
        ),
    ]
