# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='city',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='chinese_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_name',
            new_name='english_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='your home address', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='Female', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='home_number',
            field=models.CharField(default='0987xxooox', max_length=200),
        ),
    ]