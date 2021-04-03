# coding: utf-8
from django.conf.urls import patterns

urlpatterns = patterns('catalogos.views',    
    (r'^modelos/$', 'modelos'),
    (r'^modelos/add/$', 'modelosadd'),
    (r'^modelos/edit/(?P<modelo_id>\d+)/$', 'modelosedit'),

    
    (r'^modelos/delete/(?P<modelo_id>\d+)/$', 'modelosdelete'),
    (r'^economicos/$', 'economicos'),
    (r'^economicos/add/$', 'economicosadd'),
    
    (r'^economicos/edit/(?P<economico_id>\d+)/$', 'economicosedit'),
    (r'^economicosImg/edit/(?P<economico_id>\d+)/$', 'economicosImg'),
    (r'^economicos/delete/(?P<economico_id>\d+)/$', 'economicosdelete'),
    (r'^operadores/$', 'operadores'), 
    (r'^operadores/add/$', 'operadoresadd'),
    (r'^operadores/edit/(?P<operador_id>\d+)/$', 'operadoresedit'),
    (r'^operadores/delete/(?P<operador_id>\d+)/$', 'operadoresdelete'),
    (r'^casetas/$', 'casetas'), 
    (r'^casetas/add/$', 'casetasadd'),
    (r'^casetas/edit/(?P<caseta_id>\d+)/$', 'casetasedit'),
    (r'^casetas/delete/(?P<caseta_id>\d+)/$', 'casetasdelete'),
    (r'^gastos/$', 'gastos'), 
    (r'^gastos/add/$', 'gastosadd'),
    (r'^gastos/edit/(?P<gasto_id>\d+)/$', 'gastosedit'),
    (r'^gastos/delete/(?P<gasto_id>\d+)/$', 'gastosdelete'),
    (r'^aseguradoras/$','asegura'),
    (r'^aseguradoras/add/$','aseguradoraadd'),
    (r'^aseguradoras/edit/(?P<aseguradora_id>\d+)/$','aseguradorasedit'),
    (r'^aseguradoras/del/(?P<aseguradora_id>\d+)/$','aseguradoradelete'),
    (r'^conceptos/$', 'conceptos'), 
    (r'^conceptos/add/$', 'conceptosadd'),
    (r'^conceptos/edit/(?P<concepto_id>\d+)/$', 'conceptosedit'),
    (r'^conceptos/delete/(?P<concepto_id>\d+)/$', 'conceptosdelete'),
    (r'^ExcelEconomicoView/$', 'ExcelEconomicoView'),
    (r'^movUnidad/$','movUnidad'),
    (r'^documentosEconomico/(?P<economico_id>\d+)/$', 'documentosEconomico'),
    (r'^descargaDoc/(?P<nombreArchivo>[\w.-:/+]{0,256})/$', 'descargarDoc'),
    (r'^borrarDoc/(?P<nombreArchivo>[\w.-:/]{0,256})/(?P<economico_id>\d+)/$', 'borrarDoc'),
    (r'^documentos/$','index_docs'), ### Ofa
    (r'^documentos/add/$','documentos_add'), ## Ofa 
    (r'^documentos/edit/(?P<catdoc_id>\d+)/$','docu_edit'), ## Ofa
    (r'^documentos/del/(?P<catdoc_id>\d+)/$','docu_del'), ## Ofa
    (r'^documentos/pdf/(?P<economico_id>\d+)/$','generaPdfEconomico'),
    (r'^reportesuni/$','unidadesXLS'),
    (r'^unidades/$','reportUnidades'),
    (r'^repmov/$','repMovUni'),
    (r'^movimientos/$','verMovimientos'),
)
