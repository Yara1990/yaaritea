# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170515_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(blank=True, upload_to='category/'),
        ),
    ]
