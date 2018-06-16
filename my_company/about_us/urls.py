from django.conf.urls import url
from about_us import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'about_us'

urlpatterns = [
    url(r'^about_us/$', views.about_us, name='about_us'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
