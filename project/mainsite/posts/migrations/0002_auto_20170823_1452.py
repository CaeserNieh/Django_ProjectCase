# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='date',
            new_name='group',
        ),
    ]
