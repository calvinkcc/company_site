"""my_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, StaticViewSitemap

sitemaps = {
    'posts' : PostSitemap,
    'static' : StaticViewSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='index'),
    url(r'^home/',include('home.urls',namespace='home')),
    url (r'^home/', include('django.contrib.auth.urls')),
    url(r'^contact_us/',include('contact_us.urls',namespace='contact_us')),
    url(r'^about_us/',include('about_us.urls',namespace='about_us')),
    url(r'^services/',include('services.urls',namespace='services')),
    url(r'^features/',include('features.urls',namespace='features')),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url (r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
