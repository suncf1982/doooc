# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-30 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0007_auto_20180830_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='download_times',
            field=models.IntegerField(default=0, verbose_name='下载次数'),
        ),
    ]