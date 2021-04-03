from django.conf.urls import patterns, url
from empleados.views import credencialPdf

urlpatterns = patterns ('externo.views',
	(r'^cuestionario/(?P<idSolicitante>\d+)/$','cuestionario'),
	(r'^cuestionario2/(?P<idSolicitante>\d+)/$','cuestionario2'),
	(r'^solicitudEmpleo/(?P<idSolicitante>\d+)/$','solicitudEmpleo'),
	(r'^solicitudEmpleo2/(?P<idSolicitante>\d+)/$','solicitudEmpleo2'),

)
