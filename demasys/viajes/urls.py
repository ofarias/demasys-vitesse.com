# coding: utf-8
from django.conf.urls import patterns, url
from viajes.views import CartaPorteView, IncidenteView

urlpatterns = patterns('viajes.views',    
    (r'^add/$', 'agregar'),    
    (r'^edit/(?P<viaje_id>\d+)/$', 'editar'),
    (r'^carga/$', 'carga'),
    (r'^cargaedit/(?P<viaje_id>\d+)/$', 'cargaedit'),    
    (r'^historial/(?P<viaje_id>\d+)/$', 'historial'),   
    (r'^actualizar/(?P<viaje_id>\d+)/$', 'actualizar'),
    (r'^solicitado/(?P<viaje_id>\d+)/$', 'solicitado'),  
    (r'^salida/(?P<viaje_id>\d+)/$', 'salida'),
    (r'^llegada/(?P<viaje_id>\d+)/$', 'llegada'),  
    (r'^entrega/(?P<viaje_id>\d+)/$', 'entrega'),
    (r'^facturado/(?P<viaje_id>\d+)/$', 'facturado'),
    (r'^comprobantes/(?P<viaje_id>\d+)/$', 'comprobante'), 
    (r'^gasto/(?P<gasto_id>\d+)/$', 'comprobantegasto'),
    (r'^comprobante/upload/(?P<gasto_id>\d+)/$', 'comprobante_upload'),
    (r'^comprobante/delete/(?P<comprobante_id>\d+)/$', 'comprobante_delete'),   
    (r'^cambio/(?P<viaje_id>\d+)/$', 'cambio'),   
    (r'^rutas/$', 'rutas'), 
    (r'^rutas/add/$', 'rutasadd'),
    (r'^rutas/modal/$', 'rutasmodal'),
    (r'^rutas/add/(?P<ruta_id>\d+)$', 'rutasadd'),    
    (r'^rutas/edit/(?P<ruta_id>\d+)/$', 'rutasedit'),
    (r'^reportes/$', 'reportes'),
    (r'^subirExcel/$', 'subirExcel'),
    (r'^reportes/results/$', 'reportesresults'),
    (r'^reportes/reportsexcel/$', 'reportsexcel'),
    (r'^pdfs/(?P<viaje_nombre>[a-zA-Z0-9_.-]+)/$', 'reportPdf'),
    (r'^listadoPdf/$', 'listadoPdf'),
    (r'^subirPDFMasivo/$', 'subirPDFMasivo'),
    (r'^pagPdf/$','pagPdf'),
    ##(r'^subirPDFMasivo/$','pagPdf'),
    url(r"^carta_porte/(?P<pk>\d+)/$", CartaPorteView.as_view(), name='carta_porte'),
    url(r"^incidente/(?P<pk>\d+)/$",IncidenteView.as_view(), name='incidente'),
    (r'^$', 'index'),
    (r'^fact/$','index_fact'),
    (r'^colocarMensaje/(?P<cliente_id>\d*)/(?P<archivo>[a-zA-Z0-9_.-]+)/$', 'colocarMensaje'),
    (r'^reporteManiobras/$','reporteManiobras'),
    (r'^generaReporteMani/$','generaReporteMani'),
    (r'^movs/$','index_movs'),
    (r'^addmov/$', 'agregarMov'),
    (r'^editmov/(?P<movimiento_id>\d+)/$', 'editMov'),
    (r'^addmovuni/$','agregaMovimiento'),
    (r'^movimientos/$','verMovimientos'),
    (r'^incidentes/$','indexIncidentes'),
    (r'^rechazar/(?P<idReporteUnidad>\d+)/(?P<estatus>\d+)/$','statusIncidente'),
    (r'^liberar/','liberarViaje'),
    (r'^lib/$','liberar'),
    (r'^impreporte/$','RepIncidentes'),
    (r'^generaReporteInc/$','imprimeIncidentes'),
    (r'^editarMov/(?P<incidente_id>\d+)/$','editarMov'),
    (r'^revisarMov/(?P<incidente_id>\d+)/$','revisarMov'),
    (r'^indexXLS/$','indexXLS'),
    (r'^desXLS/(?P<nombreArchivo>[\w./+]{0,256})/$','descargarXLS'),
    (r'^archivos/$','indexArchivos'),
    (r'^add_file/$','agregaArchivo'),
    (r'^del_file/(?P<archivo_id>\d+)/$', 'del_file'),
    (r'^descargaArchivo/(?P<nombreArchivo>[\w./+]{0,256})/$', 'descargarArchivo'),
    (r'^viajesAbiertos/$','viajesAbiertos'),
    (r'^listadoFacturas/$','facturasIndex'),
    (r'^subirXLS/$','subirXLS'),
    (r'^index_viajes_doc/$','index_viajes_doc'),
    (r'^cambiaDoc/(?P<pk>\d+)/(?P<status_doc>\d+)/$','cambia_doc'),
    (r'^imprepcerrados/$','impRepCerrados'),
    (r'^agregarSolicitudes/$','agregarSolicitudes'),
    (r'^subirPrefacturas/$','subirPrefacturas'),
    (r'^prefacturasCargadas/$','prefacturasCargadas'),
    (r'^revisionPrefactura/(?P<fecha>\d+)/$','revisionPrefactura'),
    (r'^descargarMachote/(?P<nombreArchivo>[\w./+]{0,256})/$', 'descargarMachote'),
    (r'^cambia_doc_hold_screen/$','cambia_doc_hold_screen'),
    ##(r'^descargaDoc/(?P<nombreArchivo>[\w./+]{0,256})/$', 'descargarDoc'),

)
