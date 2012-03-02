# -*-coding:utf-8 -*-

from django.views.generic.simple import direct_to_template

__all__ = [
    'home',
]

def home(request):    
    return direct_to_template(request, 'home/index.html')