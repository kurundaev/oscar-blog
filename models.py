# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    text = models.TextField()
    photo = models.ImageField(upload_to='blog', blank=True, null=True)
    enable = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('dashboard:blog')

    def __unicode__(self):
        return self.title
