from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    url(r'^blog_1/$', views.blog_1.as_view(), name='blog_1'),
    url(r'^blog/$', views.blog.as_view(), name='blog'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
