from django.conf.urls import patterns

urlpatterns = patterns ('solicitudes.views',
	(r'^add/$','agregar'),
	(r'^$','index'),
	(r'^edit/(?P<solicitudes_id>\d+)/$', 'editar'),
	(r'^aut/(?P<solicitudes_id>\d+)/$', 'asignar'),
	(r'^cancelar/$','cancelar_index'),
	(r'^cancel/(?P<solicitudes_id>\d+)/$','cancelar'),
	(r'^rep_sol/$', 'reporte_sol'),
	(r'^rep_sol_xls/$','reportsexcel'),
	(r'^rep_sol_result/$','reportesresults'),
	(r'^conceptos/','index_con'),
	(r'^add_con/$','agregar_con'),
	(r'^edit_con/(?P<Conceptos_id>\d+)/$','editar_con'),
	(r'^editar/(?P<solicitudes_id>\d+)/$','edit'),
	(r'^autorizar/(?P<solicitudes_id>\d+)/$','autorizar'),
	(r'^cuenta_banco/$','cuenta_banco'),
	(r'^reporteGastos/$','reporteGastos'),
	(r'^generaReporte/$','generaReporte'),
	(r'^reporteContable/$','reporteContable'),
	(r'^index_pendientes/$','index_pendientes'),
	(r'^index_comprobantes/$','index_comprobantes'),
	(r'^subirArchivoPendiente/(?P<idSolicitud>\d+)/(?P<tipo>\w+)/$','subirArchivoPendiente'),
	(r'^descargaDoc/(?P<nombreArchivo>[\w./+]{0,256})/$', 'descargarDoc'),
	##(r'^historial/(?P<solicitudes_id>\d+)/$','historial'),
)
