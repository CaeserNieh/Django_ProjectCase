# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('date', models.CharField(max_length=200)),
            ],
        ),
    ]
