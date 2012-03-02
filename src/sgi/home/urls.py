# -*-coding:utf-8 -*-

from django.conf.urls.defaults import *
from shortcuts import route

urlpatterns = patterns('home.views',    
    url(r'', 'home', name='home'),
)