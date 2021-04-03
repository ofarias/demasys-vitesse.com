# coding: utf-8
#from django.conf.urls import patterns
from django.conf.urls import patterns, url
from reporte.views import ReporteMensualView

urlpatterns = patterns('reporte.views',
    (r'^agregar$', 'agregar'),
    (r'^agregarBruta/(?P<idReporte>\d+)/$', 'agregarBruta'),
    (r'^agregarNeta/(?P<idReporte>\d+)/$', 'agregarNeta'),
	(r'^generarReporte/(?P<idReporte>\d+)/$','generarReporte'),
	(r'^agregarNomina/(?P<idReporte>\d+)/$', 'agregarNomina'),
	(r'^generaPresentacion$','obtenerDatos'),
	(r'^index$','indexReportes'),
	url(r"^reportes/(?P<pk>\d+)/$", ReporteMensualView.as_view(), name='reportes'),
)
