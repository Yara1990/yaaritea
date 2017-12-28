# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.
from django.db.models import permalink


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    content_photo = models.ImageField(upload_to='media/blog_image/', blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    author = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'blog:view_blog_post', None, {'slug': self.slug}


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    category_photo = models.ImageField(upload_to='media/category_image/', blank=True)
    # img_path = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return '%s' % self.title

    # def get_absolute_url(self):
    #     try:
    #         url = reverse('view_blog_post', args=[self.slug])
    #     except Exception as e:
    #         print e
    #     return 'view_blog_post', None, {'slug': self.slug}

    @models.permalink
    def get_absolute_url(self):
        return 'blog:view_blog_category', (), {'slug': self.slug}
