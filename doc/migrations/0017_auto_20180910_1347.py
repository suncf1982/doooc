# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-10 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0016_auto_20180910_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='docs',
            field=models.ManyToManyField(blank=True, null=True, to='doc.Doc', verbose_name='文档'),
        ),
    ]
