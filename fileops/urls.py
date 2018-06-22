# _*_ encoding:utf-8 _*_
from django.conf.urls import url

from .views import get_name, send_email


urlpatterns = [
    url(r'getname/$', get_name, name='getname'),
    url(r'sendmail/$', send_email, name='sendmail'),
]
