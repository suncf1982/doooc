# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-28 15:52
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('doc', '0002_auto_20180828_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签'),
        ),
    ]
