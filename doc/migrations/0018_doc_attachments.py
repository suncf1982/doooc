# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-14 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180830_1638'),
        ('doc', '0017_auto_20180910_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='attachments',
            field=models.ManyToManyField(blank=True, null=True, to='core.Resource', verbose_name='附件'),
        ),
    ]
