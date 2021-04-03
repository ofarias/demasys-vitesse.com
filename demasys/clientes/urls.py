# coding: utf-8
from django.conf.urls import patterns

urlpatterns = patterns('clientes.views',        
    (r'^add/$', 'agregar'),
    (r'^edit/(?P<cliente_id>\d+)/$', 'editar'),    
    (r'^departamentos/edit/(?P<departamento_id>\d+)/$', 'departamentoedit'),
    (r'^departamentos/add/(?P<cliente_id>\d+)/$', 'departamentoadd'),
    (r'^departamentos/(?P<cliente_id>\d+)/$', 'departamentos'),
    (r'^recoleccion/(?P<cliente_id>\d+)/$', 'recoleccion'),
    #(r'^delete/(?P<cliente_id>\d+)/$', 'eliminar'),    
    (r'^$', 'index'),
)