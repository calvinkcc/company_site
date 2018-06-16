# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators

class Contact(models.Model):
    reason_contact = (
        ('S', 'Services'),
        ('B', 'Business Inquiries'),
        ('O', 'Others'),
    )
    reason_of_contact = models.CharField(max_length=1,choices = reason_contact)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, validators=[validators.validate_email])
    subject = models.CharField(max_length=250)
    textarea = models.TextField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def __str__(self):
        return self.name
