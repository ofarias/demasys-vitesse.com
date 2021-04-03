from django.conf.urls import patterns, url
from empleados.views import credencialPdf

urlpatterns = patterns ('empleados.views',
	(r'^add/$','agregar'),
	(r'^$','index'),
        (r'^operadores/$','operadores'),
	(r'^edit/(?P<empleado_id>\d+)/$', 'editar'),
	(r'^solempleados/$','solempleados'),
	(r'^secDocumentacion/(?P<idSolicitante>\d+)/$','secDocumentacion'),
	(r'^secHabitos/(?P<idSolicitante>\d+)/$','secHabitos'),
	(r'^secFamiliares/(?P<idSolicitante>\d+)/$','secFamiliares'),
	(r'^secEscolaridad/(?P<idSolicitante>\d+)/$','secEscolaridad'),
	(r'^secConocimientos/(?P<idSolicitante>\d+)/$','secConocimientos'),
	(r'^secEmpleos/(?P<idSolicitante>\d+)/$','secEmpleos'),
	(r'^secReferencias/(?P<idSolicitante>\d+)/$','secReferencias'),
	(r'^secGenerales/(?P<idSolicitante>\d+)/$','secGenerales'),
	(r'^secEconomico/(?P<idSolicitante>\d+)/$','secEconomico'),
	(r'^documentosEmpleado/(?P<empleado_id>\d+)/$', 'documentosEmpleado'),
	(r'^descargaDoc/(?P<nombreArchivo>[\w./+]{0,256})/$', 'descargarDoc'),
	(r'^borrarDoc/(?P<nombreArchivo>[\w./]{0,256})/(?P<empleado_id>\d+)/$', 'borrarDoc'),
	url(r"^credencial/(?P<pk>\d+)/$", credencialPdf.as_view(), name='credencial'),
	(r'^fotosEmpleado/(?P<empleado_id>\d+)/$', 'fotosEmpleado'),
        (r'^documentos/$','index_docs'), ### Ofa
        (r'^documentos/add/$','documentos_add'), ## Ofa 
        (r'^documentos/edit/(?P<catdoc_id>\d+)/$','docu_edit'), ## Ofa
        (r'^documentos/del/(?P<catdoc_id>\d+)/$','docu_del'), ## Ofa
        (r'^puestos/$','index_p'),  # OFA
        (r'^puestos/add/$','puesto_add'),  ##OFA
        (r'^puestos/edit/(?P<puestos_id>\d+)/$','puesto_edit'), ## OFA
        (r'^puestos/del/(?P<puestos_id>\d+)/$','puesto_del'),  ## Ofa
        (r'^movempadd/$','movimiento_emp'),
	(r'^expediente/(?P<empleado_id>\d+)/$','generaPdfEmpleado'),
	(r'^cuestionario/(?P<idSolicitante>\d+)/$','cuestionario'),
	(r'^cuestionario2/(?P<idSolicitante>\d+)/$','cuestionario2'),
	(r'^solicitudEmpleo/$','solicitudEmpleo'),
	(r'^solicitudEmpleo2/(?P<idSolicitante>\d+)/$','solicitudEmpleo2'),
	(r'^solicitudeslista/$','solicitudeslista'),
	(r'^cambiarEstatus/(?P<idSolicitante>\d+)/(?P<estatus>\d+)/$','cambiarEstatus'),
	(r'^generarPdfSolicitud/(?P<idSolicitante>\d+)/$','generarPdfSolicitud'),
	(r'^validaArchivos/(?P<pk>\d+)/$','validaArchivos'),
)
