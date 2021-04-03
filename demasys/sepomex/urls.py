# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('sepomex.views',
    (r'^direccion/$','direccion'),
    (r'^direccion-recupera/$','direccion_recupera'),
    (r'^direccion-recupera-unico/$','direccion_recupera_unico'),
    (r'^estados.js$','estados'),
    (r'^cp/search/(?P<cp>\d+)/$','get_by_cp'),
    (r'^colonias/$','colonias'),
    (r'^cp/$','cp'),
    (r'^map/$','map'),
)