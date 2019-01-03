# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None)

    
    def __str__(self):
        return self.title


    def preview(self):
        return self.body[:50] + "..."
