# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from contact_us.forms import Contact_Form
from django.views.generic import FormView,TemplateView

class contact_view(FormView):
    form_class = Contact_Form
    template_name = 'contact_us/contact_us.html'
    success_url = reverse_lazy('contact_us:contact_us')

    def form_valid(self,form):
        form.save(commit=True)
        return super(contact_view,self).form_valid(form)
