# coding: utf-8
from django.conf.urls import patterns

urlpatterns = patterns('inventario.views',
    (r'^ExcelInventario', 'ExcelInventario'),
    (r'^productos/$', 'productos'),
    (r'^productosadd/$', 'productoadd'),
    (r'^producto/edit/(?P<producto_id>\d+)/$', 'productoedit'),
    (r'^producto/delete/(?P<producto_id>\d+)/$', 'productodelete'),
    (r'^reporteMovimientos/$', 'reporteMovimientos'),
    (r'^movimientosadd/$', 'movimiento_add'),
    (r'^movimientosasig/$','movimiento_asig'),
)
