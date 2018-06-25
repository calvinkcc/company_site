# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

class blog(TemplateView):
    template_name = 'blog/blog.html'

class blog_1(TemplateView):
    template_name = 'blog/blog_1.html'
