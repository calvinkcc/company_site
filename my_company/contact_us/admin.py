# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at',)

admin.site.register(Contact,RatingAdmin)
