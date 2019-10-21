# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170530_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content_photo',
            field=models.ImageField(blank=True, upload_to='media/blog_image/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(blank=True, upload_to='media/category_image/'),
        ),
    ]