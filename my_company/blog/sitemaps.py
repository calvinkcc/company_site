from django.contrib.sitemaps import Sitemap
from .models import Blog
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    def lastmod(self,item):
        return item.date

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about_us:about_us','index','contact_us:contact_us','services:web_development','services:web_marketing','services:cabling',
                    'services:phone_fix','services:computer_fix','services:general_consultant','services:network','services:security_camera','services:other_devices',]
    def location(self,item):
        return reverse(item)
