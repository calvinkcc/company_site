# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from about_us.models import About

def about_us(request):
    name_list = About.objects.order_by('name')
    name_dict = {'name': name_list}
    return render(request,  'about_us/about_us.html',  context=name_dict)
