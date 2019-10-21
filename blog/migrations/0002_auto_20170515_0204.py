# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_photo',
            field=models.ImageField(blank=True, upload_to='passive_income/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]