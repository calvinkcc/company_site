# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=300)
    description = models.TextField()
    text = models.TextField()
    image=models.ImageField(upload_to='media/')
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail',args=[str(self.id)])
