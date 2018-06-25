from django.conf.urls import url
from services import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'services'

urlpatterns = [
    url(r'^security_camera/$', views.security_camera.as_view(), name='security_camera'),
    url(r'^other_devices/$', views.other_devices.as_view(), name='other_devices'),
    url(r'^phone_fix.html/$', views.phone_fix.as_view(), name='phone_fix'),
    url(r'^computer_fix/$', views.computer_fix.as_view(), name='computer_fix'),
    url(r'^cabling/$', views.cabling.as_view(), name='cabling'),
    url(r'^network/$', views.network.as_view(), name='network'),
    url(r'^general_consultant/$', views.general_consultant.as_view(), name='general_consultant'),
    url(r'^web_development/$', views.web_development.as_view(), name='web_development'),
    url(r'^web_marketing/$', views.web_marketing.as_view(), name='web_marketing'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
