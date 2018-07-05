# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from blog.models import Blog
from django.views.generic import DetailView


class PostDetailView(DetailView):
    model = Blog
    template_name = "blog/post.html"
