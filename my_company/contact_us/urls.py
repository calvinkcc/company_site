from django.conf.urls import url
from . import views

app_name = 'contact_us'

urlpatterns = [
    url(r'^contact_us/$', views.contact_view.as_view(), name ='contact_us'),

]
