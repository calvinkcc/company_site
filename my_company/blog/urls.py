from django.conf.urls import url
from blog import views
from django.views.generic import ListView, DetailView
from blog.models import Blog
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Blog.objects.all().order_by("-date")[:10], template_name="blog/blog.html"),name='blog_list'),
    url(r'^(?P<pk>\d+)$', views.PostDetailView.as_view(), name='blog_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
