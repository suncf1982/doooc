# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-31 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0009_doctemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日期'),
        ),
    ]