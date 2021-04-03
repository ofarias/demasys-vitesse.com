# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('dashboards.views',    
    (r'^reporte/(?P<year>\d+)/(?P<month>\d+)/$', 'reporte'),
    (r'^$', 'index'), 
)