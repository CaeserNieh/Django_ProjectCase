# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=500)),
                ('password2', models.CharField(max_length=500)),
                ('email', models.EmailField(default='xxx@gmail.com', max_length=200)),
            ],
        ),
    ]
