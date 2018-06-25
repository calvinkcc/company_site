from django.conf.urls import url
from features import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'features'

urlpatterns = [
    url(r'^features/$', views.features.as_view(), name='features'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
