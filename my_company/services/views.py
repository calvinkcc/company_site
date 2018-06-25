# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

class security_camera(TemplateView):
    template_name = 'services/security_camera.html'

class other_devices(TemplateView):
    template_name = 'services/other_devices.html'

class phone_fix(TemplateView):
    template_name ='services/phone_fix.html'

class computer_fix(TemplateView):
    template_name ='services/computer_fix.html'

class cabling(TemplateView):
    template_name ='services/cabling.html'

class network(TemplateView):
    template_name ='services/network.html'

class general_consultant(TemplateView):
    template_name ='services/general_consultant.html'

class web_development(TemplateView):
    template_name ='services/web_development.html'

class web_marketing(TemplateView):
    template_name ='services/web_marketing.html'
